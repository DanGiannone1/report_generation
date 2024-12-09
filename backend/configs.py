

report_structure = """

I. Executive Summary
Objective:

Briefly state the purpose of the report: to evaluate and compare the given generative AI agent frameworks in the context of enterprise needs.
Summarize the key findings and conclusions at a very high level, including which frameworks are best aligned with specific enterprise scenarios.
Key Highlights:

A short paragraph on where each framework excels (e.g., “langgraph excels at workflow orchestration while crewAI stands out for high-level abstraction and integrated compliance controls,” etc.).
A quick recommendation on which frameworks seem most suitable for your organization’s core needs.
II. Introduction
Context and Motivation:

Explain the growing importance of generative AI agents in enterprise workflows.
Describe the organizational objectives: scalability, security, compliance, developer experience, TCO (Total Cost of Ownership), etc.
Introduce the candidate frameworks: langgraph, crewAI, autogen, semantic kernel, and llama-workflows, and why these were chosen (popularity, feature set, alignment with strategic goals).
Scope and Limitations:

State the boundaries of the comparison: versions considered, evaluation criteria, types of applications (e.g., text-based customer support, code generation, knowledge management), and any assumptions.
III. Evaluation Criteria
Technical Dimensions:

Architecture & Design Philosophy: Centralized vs. decentralized workflows; modularity; extensibility.
Integration & Compatibility: Support for various LLMs, plug-ins, vector databases, DevOps pipelines, and APIs.
Performance & Scalability: Response latency, load handling, and resource utilization efficiency.
Reliability & Robustness: Error handling, fallback models, retry mechanisms, monitoring and alerting features.
Security & Compliance: Data encryption at rest and in transit, role-based access controls, integration with enterprise authentication (SSO, OAuth), compliance certifications (HIPAA, GDPR, SOC 2).
Model Management: Versioning, model swapping, fine-tuning, prompt management and templating.
Developer Experience: Tooling, documentation quality, debugging utilities, local testing frameworks, community support.
Extensibility & Customization: Plugin ecosystems, scripting capabilities, pipeline configuration, workflow orchestration ease.
Cost & Licensing: Open-source vs. commercial licensing, total cost, support costs, and pricing models.
Organizational & Strategic Dimensions:

Vendor Stability & Ecosystem: Community health, vendor track record, maintenance frequency, alignment with industry standards.
Long-Term Viability: Roadmap transparency, future-proofing, adaptability to new LLMs or emerging standards.
Change Management & Training: The ease of onboarding teams, availability of training materials, and required skill sets.
IV. Deep-Dive Analysis per Framework
For each framework, create a structured sub-section:

A. langgraph
Overview & Core Concepts: What is langgraph and what unique capabilities does it offer?
Architecture & Integration: How does it integrate into existing enterprise workflows? Which LLMs and data sources are supported?
Features & Standouts: Pipeline definition, error handling, prompt templating, etc.
Pros/Cons (with evidence): Specific advantages (e.g., intuitive pipeline configuration) and disadvantages (e.g., limited support for certain LLMs or weaker monitoring tools).
Ideal Use Cases: Which scenarios does langgraph excel in (e.g., content moderation pipelines, complex multi-step reasoning tasks)?
Limitations & Gaps: Known issues, complexity of setup, or lack of certain enterprise-friendly features.
B. crewAI
Repeat the structure above: Overview, Features, Pros/Cons, Integration, Ideal Use Cases, Limitations.
C. autogen
Repeat the structure above.
D. semantic kernel
Repeat the structure above.
E. llama-workflows
Repeat the structure above.
V. Comparative Analysis
Tabular Comparison:

Present a matrix that scores or at least qualitatively rates each framework against the evaluation criteria.
For example, columns: Architecture Flexibility, Integration Ease, Performance, Security & Compliance, Model Management, Dev Experience, Extensibility, TCO, Ecosystem Health.
Rows: Each framework.
Provide short notes explaining the ratings.
Dimension-by-Dimension Analysis:

Architecture & Performance: Which frameworks handle large workloads best, and why?
Security & Compliance: Which frameworks have robust enterprise-grade security features out-of-the-box?
Model Management & Extensibility: Which frameworks are easiest to extend with custom logic or integrate new model endpoints?
Developer Experience & Usability: Which frameworks provide the best documentation, tooling, and developer community support?
Cost & Licensing Considerations: Which are open-source with permissive licenses vs. commercial? What are the hidden or downstream costs?
Strategic Positioning:

For certain enterprise verticals (e.g., finance, healthcare, retail), note if any framework is better suited due to compliance, performance, or ecosystem.
VI. Implementation Considerations
Integration Strategies:

Discuss the technical effort required to integrate each framework with existing enterprise systems (e.g., CRM, ERP, data lakes).
Mention any migration paths or best practices suggested by the framework documentation or community.
Operationalization:

How easy is it to move from prototype to production using each framework?
Observability: Metrics, logging, tracing.
Ongoing maintenance: Upgrades, patching, and handling new LLM releases.
Risk Management & Vendor Lock-In:

Assess how difficult it would be to switch frameworks later.
Evaluate if the framework relies heavily on a single vendor’s stack, causing lock-in.
VII. Case Studies or Hypothetical Scenarios
Scenario 1 (Customer Support Chatbot):

Evaluate how each framework would handle a typical enterprise customer support scenario, including integration with a customer database and retrieval-augmented generation.
Scenario 2 (Internal Knowledge Base Assistant):

Compare how each framework deals with role-based access control to sensitive information and how easy it is to plug in internal data sources.
Scenario 3 (Code Generation/Developer Enablement):

Assess which framework best supports prompt templates, versioning, and testing for code-generation tasks.
VIII. Recommendations
Strategic Fit:

Based on your organization’s priorities (scalability, compliance, cost), provide a short recommendation:
Which frameworks to focus on in a proof-of-concept?
Which ones align with long-term architectural vision?
Decision Matrix:

Offer a weighted scoring system that aligns your organization’s priorities with the evaluation criteria. Present a final score or short list of recommended frameworks.
IX. Conclusion
Summary of Findings:

Reiterate the main differences among the frameworks, their trade-offs, and how these align with your enterprise goals.
Next Steps:

Suggest a PoC or pilot project with the top one or two frameworks.
Outline timelines for a more thorough hands-on evaluation and vendor outreach.
X. Appendices
Technical Reference Sheets:

Quick feature checklists, API references, or code snippet comparisons.
Glossary:

Define any specialized terms used throughout the report (e.g., RAG—Retrieval Augmented Generation).
Bibliography & Resources:

Links to official documentation, community forums, and industry reports.


"""



# Prompt generating the report outline
section_generation_prompt="""You are a report outline parser. 

Your goal is to take a topic and a report outline, and parse the outline into the individual sections of the report. Analysts will take each section and go off to do their research.

The overall topic of the report is:

{topic}

The report outline is as follows: 

{report_structure}


<end report structure>

You should reflect on this information to plan the sections of the report: 

{context}

Now, generate the sections of the report. Each section should have the following fields:

- Name - Name for this section of the report (parsing).
- Description - Brief overview of the main topics and concepts to be covered in this section (parsing).
- Research - Whether to perform web research for this section of the report (use your judgement, answer true/false).
- Content - The content of the section (leave blank for now).

Consider which sections require web research. For example, executive summary and conclusion will not require research because they will distill information from other parts of the report. Introduction might however. The content sections almost certainly will require research, but necessarily if they are about a topic from the past (before 2022).

The most important point to remember is that you parsing each section of the report into a structured format, so you must capture all of the text verbatim in each section. 
Capture the top-level headers in the table of contents, and load the text under that into the description field.

"""

# Prompt generating the report outline
research_query_prompt="""You are a researcher tasked with gathering information for a report. You will be given the background info such as the report topic and the report outline, and a specific section of the report to research.  

Your job is to generate a list of search queries that will be used to find information on the web related to the section topic. Generate up to 4 search queries that you think will best provide the necessary info.

The overall topic of the report is:

{topic}

Your specific section to research is as follows: 

{section_name}
{section_description}

Here is what we have written thus far (might be blank if first attempt):

{section_content}

Please consider the following feedback when generating your search queries (this is coming from someone reviewing what you have written so far):

{feedback}

"""

research_writing_prompt="""You are a researcher tasked with gathering information for a report. You will be given the background info such as the report topic, the report outline, 
the specific section of the report we are researching, and the current research material thus far. 

The overall topic of the report is:

{topic}

Your specific section to write about is as follows: 

{section_name}
{section_description}

Here is what we have written thus far (might be blank if first attempt):

{section_content}

Please use the following information to write this section of the report:

{research_material}

<end research material>

Guidelines for writing:

Style:
- Provide as much detail as possible to ensure the section is comprehensive, but do not repeat yourself or include irrelevant information.
- No marketing language
- Technical focus
- Start with your most important insight in **bold**

Structure:
- Write in valid markdown syntax
- Only use the information provided. 
- Use ## for section title (Markdown format)
- Use structural elements ONLY IF they helps clarify your point:
  * A focused table comparing 2-3 key items (using Markdown table syntax)
  * A short list (3-5 items) using proper Markdown list syntax:
    - Use `*` or `-` for unordered lists
    - Use `1.` for ordered lists
    - Ensure proper indentation and spacing
- Cite your sources and then list them at the bottom of your response. You can include citations like [1], [2], etc in the text, then cite at the bottom.
- End with ### Sources that references the below source material formatted as:
  * List each source with title, date, and URL
  * Format: `- Title : URL`




"""


research_feedback_prompt="""You are a researcher tasked with evaluating the progress of information gathering for a report section. 
You will be given the background info such as the report topic, the report outline, the specific section of the report we are researching, and the current progress thus far.
Your job is to determine if we have sufficiently researched the section, or if we need to continue researching. If we have a thorough, comprehensive section, you should finalize it. 
If we need more information or there are issues with the current content, you should continue researching.

The overall topic of the report is:

{topic}

The specific section to research is as follows: 

{section_name}
{section_description}

The current content we have written is as follows:

{section_content}

Your output should be in the following format: 

thought_process: <your thought process here>
answer: If we have enough info, answer "finalize". If we need more info, answer "continue_research".

"""


final_approval_prompt="""Your job is to finalize a report section. You will be given the background info such as the report topic, the specific section of the report we are researching, 
and the current write-up of the section. Your job is to determine if it is fine as is, or if it needs to be revised. Sometimes the content may not flow well and may need to be rewritten. 
Other times it will be perfect. Make sure it is in valid markdown syntax with logical structure and good readability.


The overall topic of the report is:

{topic}

The specific section to research is as follows: 

{section_name}
{section_description}

The current write-up is as follows:

{section_content}

Your output should be in the following format: 

thought_process: <your analysis of the section write-up here>
answer: If it is perfect as is, answer "approved". If not, rewrite the section to make it better. Make sure to include all the same information and the sources/citations.

"""


intro_conclusion_instructions = """You are a technical writer finishing a report on {topic}

You will be given all of the sections of the report.

You job is to write a crisp and compelling introduction or conclusion section.

The user will instruct you whether to write the introduction or conclusion.

Include no pre-amble for either section.

Target around 300-400 words, crisply previewing (for introduction) or recapping (for conclusion) all of the sections of the report.

Use markdown formatting. 

For your introduction, create a compelling title and use the # header for the title.

For your introduction, use ## Introduction as the section header. 

For your conclusion, use ## Conclusion as the section header.

Here are the sections to reflect on for writing: 

{report_body}"""