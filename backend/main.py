#main.py
# Imports
import asyncio
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from typing_extensions import TypedDict
import langgraph
from typing import List, Annotated, Optional, Literal
from pydantic import BaseModel, Field
import operator
import langsmith
from tavily import TavilyClient, AsyncTavilyClient

from langchain_core.runnables import RunnableConfig
from langgraph.constants import Send
from langgraph.graph import START, END, StateGraph
from langsmith import traceable
from dataclasses import dataclass, field, fields
from typing import Any

from markdown import markdown
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak


from configs import *
from create_pdf import markdown_to_pdf_enhanced

# Environment and Configuration Setup
load_dotenv()

# Azure OpenAI configuration
aoai_deployment = os.getenv("AOAI_DEPLOYMENT")
aoai_key = os.getenv("AOAI_KEY")
aoai_endpoint = os.getenv("AOAI_ENDPOINT")

# Other environment variables
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Client Initializations
llm = AzureChatOpenAI(
    azure_deployment=aoai_deployment,
    api_version="2024-08-01-preview",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=aoai_key,
    azure_endpoint=aoai_endpoint
)

tavily_client = TavilyClient()
tavily_async_client = AsyncTavilyClient()

# Data Models/Schemas
class FeedbackResponse(BaseModel):
    """Schema for feedback response"""
    thought_process: str
    answer: Literal["continue_research", "finalize"]

# Data Models/Schemas
class ReasoningResponse(BaseModel):
    """Schema for feedback response"""
    thought_process: str
    answer: str

class ReportState(TypedDict):
    topic: str
    report_structure: str
    sections: List[str]
    completed_sections: Annotated[list, operator.add]
    introduction: str
    report_body: str
    conclusion: str
    final_report: str

class Section(BaseModel):
    name: str = Field(description="Name of this section of the report")
    description: str = Field(description="Brief overview of the main topics and concepts to be covered in this section")
    research: bool = Field(description="Whether to perform web research for this section of the report or not (true/false)")
    content: str = Field(description="Content of this section of the report")

class Sections(BaseModel):
    sections: List[Section] = Field(description="List of the sections of the report")

class SearchQueries(BaseModel):
    queries: List[str] = Field(
        description="List of search queries. Generate up to 5 search queries.",
    )



class ResearchState(TypedDict):
    topic: str
    report_structure: str
    section: Section
    search_queries: SearchQueries
    feedback: FeedbackResponse
    iteration_counter: int
    completed_sections: list[Section]

class ResearchOutputState(TypedDict):
    completed_sections: list[Section]



# Report Generation Functions
def generate_report_structure(state: ReportState):
    """Generates the report structure"""
    print("Generating report structure for user input: \n\n", state['topic'])
    #state["report_structure"] = report_structure
    return {'report_structure': state["report_structure"]}

def generate_section_list(state: ReportState):
    """Generates the list of sections"""
    structured_llm = llm.with_structured_output(Sections)
    section_generation_system_prompt = section_generation_prompt.format(
        topic=state['topic'], 
        report_structure=state['report_structure'], 
        context=""
    )
    sections = structured_llm.invoke([
        SystemMessage(content=section_generation_system_prompt)
    ] + [HumanMessage(content="Populate the sections")])
    state["sections"] = sections.sections
    return {'sections': state["sections"]}


# Utility Functions
def deduplicate_and_format_sources(search_response, max_tokens_per_source, include_raw_content=True):
    """Takes either a single search response or list of responses from Tavily API and formats them."""
    # [Function implementation remains the same]
    if isinstance(search_response, dict):
        sources_list = search_response['results']
    elif isinstance(search_response, list):
        sources_list = []
        for response in search_response:
            if isinstance(response, dict) and 'results' in response:
                sources_list.extend(response['results'])
            else:
                sources_list.extend(response)
    else:
        raise ValueError("Input must be either a dict with 'results' or a list of search results")
    
    unique_sources = {}
    for source in sources_list:
        if source['url'] not in unique_sources:
            unique_sources[source['url']] = source
    
    formatted_text = "Sources:\n\n"
    for i, source in enumerate(unique_sources.values(), 1):
        formatted_text += f"Source {source['title']}:\n===\n"
        formatted_text += f"URL: {source['url']}\n===\n"
        formatted_text += f"Most relevant content from source: {source['content']}\n===\n"
        if include_raw_content:
            char_limit = max_tokens_per_source * 4
            raw_content = source.get('raw_content', '')
            if raw_content is None:
                raw_content = ''
                print(f"Warning: No raw_content found for source {source['url']}")
            if len(raw_content) > char_limit:
                raw_content = raw_content[:char_limit] + "... [truncated]"
            formatted_text += f"Full source content limited to {max_tokens_per_source} tokens: {raw_content}\n\n"
                
    return formatted_text.strip()

def format_sections(sections: list[Section]) -> str:
    """ Format a list of sections into a string """
    formatted_str = ""
    for idx, section in enumerate(sections, 1):
        formatted_str += f"""
{'='*60}
Section {idx}: {section.name}
{'='*60}
Description:
{section.description}
Requires Research: 
{section.research}

Content:
{section.content if section.content else '[Not yet written]'}

"""
    return formatted_str

# Research and feedback Functions
@traceable(run_type="retriever", name="tavily_web_search")
async def tavily_search_async(query, tavily_topic="general", tavily_days=None):
    """Performs a single web search using the Tavily API."""
    # [Function implementation remains the same]
    if tavily_topic == "news":
        return await tavily_async_client.search(
            query,
            max_results=5,
            include_raw_content=True,
            topic="news",
            days=tavily_days
        )
    else:
        return await tavily_async_client.search(
            query,
            max_results=5,
            include_raw_content=True,
            topic="general"
        )

@traceable(run_type="retriever", name="web_search")
async def tavily_search_async(query: str, tavily_topic: str = "general", tavily_days: Optional[int] = None, timeout: int = 40):
    """Performs a single web search using the Tavily API with timeout handling."""
    try:
        if tavily_topic == "news":
            return await asyncio.wait_for(
                tavily_async_client.search(
                    query,
                    max_results=5,
                    include_raw_content=True,
                    topic="news",
                    days=tavily_days
                ),
                timeout=timeout
            )
        else:
            return await asyncio.wait_for(
                tavily_async_client.search(
                    query,
                    max_results=5,
                    include_raw_content=True,
                    topic="general"
                ),
                timeout=timeout
            )
    except asyncio.TimeoutError:
        print(f"Search for '{query}' timed out after {timeout} seconds")
        return None
    except Exception as e:
        print(f"Error in search for '{query}': {str(e)}")
        return None



async def conduct_research(state: ResearchState):
    """Conduct research for a section, with attempt tracking"""
    # [Function implementation remains the same]
    state['iteration_counter'] += 1
    print(f"###Conducting research for section: ```{state['section'].name}``` --- (Attempt {state['iteration_counter']})###")

    
    structured_llm = llm.with_structured_output(SearchQueries)



    system_prompt = research_query_prompt.format(
        topic=state['topic'],
        section_name=state['section'].name,
        section_description=state['section'].description,
        section_content=state['section'].content,
        feedback=state['feedback'].thought_process if state['feedback'] else ""
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please generate the search queries"}
    ]

    
    response = structured_llm.with_config({"run_name": "Generate Search Queries"}).invoke(messages)

    for query in response.queries:
        print("Search Query: ", query)
        state['search_queries'].append(query)

    search_results = await asyncio.gather(
        *[tavily_search_async(query) for query in response.queries],
        return_exceptions=True
    )

    # Filter out None results and exceptions
    filtered_results = [
        result for result in search_results 
        if result is not None and not isinstance(result, Exception)
    ]

    research = deduplicate_and_format_sources(filtered_results, max_tokens_per_source=1000, include_raw_content=False)
    #print("Research: \n\n", research)

    
    system_prompt = research_writing_prompt.format(
        topic=state['topic'],
        section_name=state['section'].name,
        section_description=state['section'].description,
        section_content=state['section'].content,
        research_material=research
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please generate the content for the section"}
    ]

    response = llm.invoke(messages)

    state['section'].content += response.content
    
    return {
        'section': state['section'],
        'search_queries': state['search_queries'],
        'iteration_counter': state['iteration_counter']
    }

def evaluate_research(state: ResearchState):
    """Evaluates the research conducted"""
    # [Function implementation remains the same]
    print("Evaluating research...")

    structured_llm = llm.with_structured_output(FeedbackResponse)

    system_prompt = research_feedback_prompt.format(
        topic=state['topic'],
        section_name=state['section'].name,
        section_description=state['section'].description,
        section_content=state['section'].content
    )

   
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please generate the content for the section"}
    ]

    
    feedback_response = structured_llm.with_config({"run_name": "Provide Feedback"}).invoke(messages)

    print("Thought Process: ", feedback_response.thought_process)
    print("Answer: ", feedback_response.answer)

    return {'feedback': feedback_response}

def finalize_research(state: ResearchState):
    """Finalizes the research"""
    print("Finalizing research...")
    structured_llm = llm.with_structured_output(ReasoningResponse)

    system_prompt = final_approval_prompt.format(
        topic=state['topic'],
        section_name=state['section'].name,
        section_description=state['section'].description,
        section_content=state['section'].content
    )

   
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please review the write-up"}
    ]

    response = structured_llm.with_config({"run_name": "Final Revisions & Approval"}).invoke(messages)

    print("Thought Process: ", response.thought_process)
    print("Answer: ", response.answer)

    if response.answer != "approved":
        state['section'].content = response.answer

    section = state['section']

    return {"completed_sections": [section]}

# Router Functions
def review_router(state: ResearchState) -> str:
    """Routes the research process based on feedback answer and attempt count."""
    MAX_ATTEMPTS = 3
    
    if state["feedback"].answer == "continue_research" and state["iteration_counter"] < MAX_ATTEMPTS:
        print(f"Continuing research (attempt {state['iteration_counter']} of {MAX_ATTEMPTS})")
        return "continue"
    
    if state["iteration_counter"] >= MAX_ATTEMPTS:
        print(f"Maximum attempts ({MAX_ATTEMPTS}) reached. Finalizing research.")
    else:
        print("Research feedback complete. Finalizing research.")
    
    return "finalize"

def distribute_sections(state: ReportState):
    """Maps each section to a research subgraph instance"""
    return [
        Send("research_agent", {
            "topic": state["topic"],
            "report_structure": state["report_structure"],
            "section": section,
            "search_queries": [],
            "feedback": None,
            "iteration_counter": 0,
            "completed_sections": []
        }) for section in state["sections"]
    ]

def consolidate_results(state: ReportState):
    """Reduces the processed sections back into the final report"""
    # Extract sections from all research results
    completed_sections = state["completed_sections"]

    report_body = ""
    for section in completed_sections:
        report_body = report_body + section.content + "\n\n"
    
    return {
        "report_body": report_body,
    }


def write_introduction(state: ReportState):
    """Writes the introduction to the report"""
    system_prompt = intro_conclusion_instructions.format(
        topic=state['topic'],
        report_body=state['report_body']
    )
   
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please write the introduction"}
    ]

    introduction = llm.invoke(messages).content

    return {"introduction": introduction}

def write_conclusion(state: ReportState):
    """Writes the conclusion to the report"""
    system_prompt = intro_conclusion_instructions.format(
        topic=state['topic'],
        report_body=state['report_body']
    )
   
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Please write the conclusion"}
    ]

    conclusion = llm.invoke(messages).content

    return {"conclusion": conclusion}

def finalize_report(state: ReportState):
    """Finalizes the report"""
    print("Finalizing report...")
    final_report = f"""
    {state['introduction']}
    {state['report_body']}
    {state['conclusion']}
    """
     
    return {"final_report": final_report}


# Research Graph
builder = StateGraph(ResearchState, output=ResearchOutputState)
builder.add_node("conduct_research", conduct_research)
builder.add_node("evaluate_research", evaluate_research)
builder.add_node("finalize_research", finalize_research)

builder.add_edge(START, "conduct_research")
builder.add_edge("conduct_research", "evaluate_research")

builder.add_conditional_edges(
    "evaluate_research",
    review_router,
    {
        "continue": "conduct_research",
        "finalize": "finalize_research"
    }
)

builder.add_edge("finalize_research", END)

research_agent = builder.compile()


# Main Report Graph
main_graph_builder = StateGraph(ReportState)

# Add nodes
# Add nodes
main_graph_builder.add_node("generate_report_structure", generate_report_structure)
main_graph_builder.add_node("generate_section_list", generate_section_list)
main_graph_builder.add_node("research_agent", builder.compile())
main_graph_builder.add_node("consolidate_results", consolidate_results)
main_graph_builder.add_node("write_introduction", write_introduction)
main_graph_builder.add_node("write_conclusion", write_conclusion)
main_graph_builder.add_node("finalize_report", finalize_report)


# Add edges
main_graph_builder.add_edge(START, "generate_report_structure")
main_graph_builder.add_edge("generate_report_structure", "generate_section_list")
main_graph_builder.add_conditional_edges("generate_section_list", distribute_sections, ["research_agent"])
main_graph_builder.add_edge("research_agent", "consolidate_results")
main_graph_builder.add_edge("consolidate_results", "write_introduction")
main_graph_builder.add_edge("consolidate_results", "write_conclusion")
main_graph_builder.add_edge("write_introduction", "finalize_report")
main_graph_builder.add_edge("write_conclusion", "finalize_report")
main_graph_builder.add_edge("finalize_report", END)
graph = main_graph_builder.compile()

graph = main_graph_builder.compile()

# Main Execution
if __name__ == "__main__":
    async def main():
        user_input = """write me a report comparing and contrasting langgraph vs CrewAI"""
        initial_state = ReportState(
            topic=user_input,
            report_structure="Features - a detailed comparison of the features of langgraph and crew AI. Use Cases - a discussion of the ideal use cases for each tool. Limitations - a comparison of the limitations of each tool. ",
            sections=[],
            completed_sections=[],
            introduction="",
            report_body="",
            conclusion="",
            final_report=""
        )


        # final_research_state = await research_agent.ainvoke(research_state)
        # return final_research_state

        final_state = await graph.ainvoke(initial_state)
        return final_state

    final_state = asyncio.run(main())
    for section in final_state["completed_sections"]:
        print(section.name)
        print(section.content)
        print("\n\n")

    print("###FINAL REPORT###")
    print(final_state["final_report"])
    

    print("Number of sections: ", len(final_state["completed_sections"]))

    markdown_to_pdf_enhanced(final_state['final_report'], "D:/data/reports/output.pdf")