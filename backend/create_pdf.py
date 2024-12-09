
from markdown import markdown
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak



report = """# LangGraph vs. AutoGen: A Comparative Analysis of AI Frameworks

## Introduction

In the rapidly evolving landscape of artificial intelligence, the development of robust frameworks for building applications with large language models (LLMs) is crucial. Two prominent frameworks, LangGraph and AutoGen, have emerged as powerful tools for developers seeking to harness the capabilities of LLMs. This report delves into a detailed comparison of these frameworks, highlighting their unique features, ideal use cases, and inherent limitations.

LangGraph is tailored for creating stateful, multi-actor applications, emphasizing agent and multi-agent workflows. Its standout features include dynamic tools integration, conditional transitions, and a robust state management system. LangGraph's architecture supports cycles, controllability, and persistence, making it highly flexible for complex scenarios. Additionally, its streaming capability allows for real-time processing of multiple conversations, enhancing its utility in production environments.

Conversely, AutoGen, developed by Microsoft, focuses on multi-agent collaboration and automation. It excels in enabling effective interaction among multiple agents, making it suitable for tasks requiring coordination among diverse AI components. AutoGen's features include native code generation and execution, a human proxy agent for integrating human feedback, and a user-friendly graphical user interface (GUI) that simplifies workflow configuration. As an open-source project, AutoGen benefits from community-driven development, fostering continuous innovation.

The report further explores the ideal use cases for each framework. LangGraph is particularly effective for applications requiring stateful, multi-actor interactions, such as conversational agents and long-running, multi-step applications. It also supports human-in-the-loop interactions and is designed for building production-ready AI agents. AutoGen, on the other hand, is suited for sophisticated problem-solving, collaborative multi-agent systems, and applications necessitating dynamic code execution, with notable applications in industries like automotive and manufacturing.

Despite their strengths, both frameworks have limitations. LangGraph's focus on language tasks may restrict its applicability in broader AI domains, and its setup complexity can pose challenges. AutoGen faces high operational costs and token limits, and its incompatibility with open-source models limits flexibility. Additionally, it requires further refinement in handling complex queries.

This report aims to provide a comprehensive understanding of LangGraph and AutoGen, equipping developers and stakeholders with the insights needed to choose the most suitable framework for their specific needs.
## Features

**LangGraph and AutoGen are both powerful frameworks for building applications with large language models (LLMs), but they offer distinct features that cater to different needs.**

### LangGraph Features

LangGraph is designed for building stateful, multi-actor applications with LLMs, focusing on creating agent and multi-agent workflows. Its key features include:

- **Dynamic Tools Integration and Conditional Transitions**: LangGraph allows for dynamic integration of tools and supports conditional transitions, which are crucial for managing complex AI workflows [1].
- **State Management**: It provides a robust framework for state management, where each node represents an LLM agent, and edges are communication channels between these agents. This structure facilitates clear and manageable workflows [2].
- **Cycles, Controllability, and Persistence**: LangGraph supports cycles in workflows, which is essential for agentic architectures, offering more flexibility compared to DAG-based solutions [3].
- **Streaming**: This feature allows for receiving results from each step of execution as separate events in a stream, which is vital for processing multiple conversations simultaneously in production applications [4].
- **Flexible Framework**: LangGraph supports diverse control flows, including single agent, multi-agent, hierarchical, and sequential, making it suitable for complex scenarios [5].

### AutoGen Features

AutoGen, developed by Microsoft, is an open-source framework that emphasizes multi-agent collaboration and automation. Its notable features include:

- **Multi-Agent Collaboration**: AutoGen excels in enabling multiple agents to interact effectively, making it ideal for tasks requiring coordination among different AI components [6].
- **Code Generation and Execution**: AutoGen supports native tool usage through code generation and execution, allowing agents to generate, run, and debug code automatically [7].
- **Human Proxy Agent**: This feature facilitates easy integration of human feedback and involvement at different levels, enhancing the adaptability of AI workflows [8].
- **Graphical User Interface (GUI)**: AutoGen minimizes the need for extensive coding by offering a GUI where users can drag and drop agents, configure workflows, and test AI-driven solutions effortlessly [9].
- **Community-Driven Development**: As an open-source project, AutoGen encourages contributions from a diverse community, fostering innovation and continuous improvement [10].

### Comparison Table

| Feature                      | LangGraph                                      | AutoGen                                      |
|------------------------------|------------------------------------------------|----------------------------------------------|
| State Management             | Robust framework with dynamic tools integration| Focus on multi-agent collaboration           |
| Workflow Flexibility         | Supports cycles and diverse control flows      | GUI for easy workflow configuration          |
| Code Execution               | Not a primary focus                            | Native support for code generation and execution |
| Human Interaction            | Not explicitly highlighted                     | Human Proxy Agent for feedback integration   |
| Community and Development    | Part of LangChain ecosystem                    | Open-source, community-driven project        |

### Sources

- [1] Revolutionizing AI Workflows: Introducing LangGraph for State Management: https://azumo.com/insights/exploring-langgraph-a-powerful-library-for-state-management-in-ai-workflows
- [2] LangGraph Tutorial: What Is LangGraph and How to Use It?: https://www.datacamp.com/tutorial/langgraph-tutorial
- [3] LangGraph - GitHub Pages: https://langchain-ai.github.io/langgraph/
- [4] From Basics to Advanced: Exploring LangGraph: https://towardsdatascience.com/from-basics-to-advanced-exploring-langgraph-e8c1cf4db787
- [5] LangGraph - LangChain: https://www.langchain.com/langgraph
- [6] Comparing Top AI Agent Frameworks: AutoGen, CrewAI, and LangGraph: https://seifeur.com/comparing-ai-agent-frameworks-autogen-crewai-langgraph/
- [7] Microsoft AutoGen: Multi-Agent AI Workflows with Advanced Automation: https://www.unite.ai/microsoft-autogen-multi-agent-ai-workflows-with-advanced-automation/
- [8] AutoGen - Microsoft Research: Overview: https://www.microsoft.com/en-us/research/project/autogen/overview/
- [9] Microsoft AutoGen: Multi-Agent AI Workflows with Advanced Automation: https://www.unite.ai/microsoft-autogen-multi-agent-ai-workflows-with-advanced-automation/
- [10] Introduction to AutoGen | AutoGen - GitHub Pages: https://microsoft.github.io/autogen/0.2/docs/tutorial/introduction/

## Use Cases

**LangGraph and AutoGen each have distinct ideal use cases, leveraging their unique capabilities to address different application needs.**

### LangGraph Use Cases

LangGraph is particularly suited for applications that require stateful, multi-actor interactions with large language models (LLMs). Its primary use cases include:

- **Conversational Agents**: LangGraph excels in building conversational agents that can handle complex dialogues and require persistent state management. This is beneficial for applications where maintaining context over multiple interactions is crucial [1].
- **Long-Running, Multi-Step Applications**: LangGraph is ideal for applications that involve long-running processes or multi-step workflows. Its support for persistent checkpoints and cycles allows for efficient management of such tasks [2].
- **Human-in-the-Loop Interactions**: Applications that require human oversight or intervention at various stages can benefit from LangGraph's built-in support for human-in-the-loop workflows [3].
- **Production-Ready AI Agents**: LangGraph is designed to build scalable and efficient AI agents suitable for real-world applications, making it a strong choice for production environments [4].

### AutoGen Use Cases

AutoGen, on the other hand, is designed to facilitate complex, multi-agent workflows with a focus on automation and collaboration. Its ideal use cases include:

- **Sophisticated Problem-Solving**: AutoGen shines in scenarios requiring advanced problem-solving capabilities, such as scientific research, bioinformatics, or climate modeling, where complex computations are common [5].      
- **Collaborative Multi-Agent Systems**: AutoGen is well-suited for applications that benefit from the synergy of multiple agents working together, sharing information, and leveraging their individual strengths to tackle complex, multi-step problems [6].
- **Code Generation and Execution**: AutoGen supports generating, executing, and debugging code automatically, making it ideal for applications that require dynamic code execution and testing [7].
- **Automotive and Manufacturing Industries**: AutoGen can be applied in industries like automotive and manufacturing for tasks such as generating and debugging code, playing chess with visual board representation, and enhanced chat capabilities for information retrieval [8].

### Sources

- [1] GitHub - langchain-ai/langgraph-example: https://github.com/langchain-ai/langgraph-example
- [2] From Basics to Advanced: Exploring LangGraph: https://towardsdatascience.com/from-basics-to-advanced-exploring-langgraph-e8c1cf4db787
- [3] LangGraph Tutorial: What Is LangGraph and How to Use It?: https://www.datacamp.com/tutorial/langgraph-tutorial
- [4] Building Production-Ready AI Agents with LangGraph: A Real-Life Use Case: https://github.com/langchain-ai/langgraph/discussions/2104
- [5] What is AutoGen? Our Guide to the Multi-Agent Platform - Skim AI: https://www.skimai.com/what-is-autogen-our-guide-to-the-multi-agent-platform-aiyou-61/
- [6] What is AutoGen? Our Full Guide to the Autogen Multi-Agent Platform: https://skimai.com/what-is-autogen-our-full-guide-to-the-autogen-multi-agent-platform/
- [7] Microsoft AutoGen: Multi-Agent AI Workflows with Advanced Automation: https://www.unite.ai/microsoft-autogen-multi-agent-ai-workflows-with-advanced-automation/
- [8] AI Agents 101 with AutoGen: Introducing Multi-Agent Conversations - xgeeks: https://blog.xgeeks.com/ai-agents-101-with-autogen/

## Limitations

**LangGraph and AutoGen, while both powerful tools for AI agent development, have distinct limitations that cater to different needs and use cases.**

### LangGraph Limitations

LangGraph is designed to handle complex task interdependencies through its graph-based approach, which excels in visualizing task interdependencies and agent relationships. However, it has specific limitations:

- **Focused Task Limitation**: LangGraph is highly specialized for language tasks, which means it may not be suitable for projects requiring broader AI capabilities, such as computer vision or predictive analytics [1].
- **Limited Scope**: Its focus on language tasks restricts its applicability to other domains, potentially limiting its versatility in multi-modal AI deployments [2].
- **Complexity in Setup**: While LangGraph Studio simplifies AI agent development, the initial setup and learning curve can be steep for those unfamiliar with graph-based frameworks [3].

### AutoGen Limitations

AutoGen, on the other hand, is known for its ability to orchestrate multi-agent conversations and maximize Large Language Model (LLM) performance. However, it also faces several limitations:

- **High Cost and Token Limits**: The use of AutoGen can be expensive due to high operational costs and token limits, which can be a significant barrier for extensive use [4].
- **Incompatibility with Open Source Models**: AutoGen's framework is not compatible with open source models, which limits its flexibility and integration with other open-source AI tools [4].
- **Refinement Needs**: AutoGen requires further refinement in understanding complex queries and handling nuanced human interactions, which can affect its performance in real-world applications [5].

### Comparative Summary

| Feature/Aspect                  | LangGraph Limitations                          | AutoGen Limitations                          |
|---------------------------------|------------------------------------------------|----------------------------------------------|
| Task Specialization             | Focused on language tasks, limited scope [1][2]| Multi-agent conversation orchestration [4]   |
| Cost and Resource Management    | Not specified                                  | High cost and token limits [4]               |
| Model Compatibility             | Supports open source LLMs                      | Incompatible with open source models [4]     |
| Complexity and Usability        | Steep learning curve for setup [3]             | Needs refinement in complex query handling [5]|

### Sources

- [1] CrewAI vs Autogen vs Langgraph. When I first used ChatGPT, I ... - Medium: https://medium.com/@isaac.casm/crewai-vs-autogen-vs-langgraph-c5d9c44f7520
- [2] Deep Dive: LangGraph vs. AutoGen - A Detailed Comparison - LinkedIn: https://www.linkedin.com/pulse/deep-dive-langgraph-vs-autogen-detailed-comparison-ravi-gupta-dzkrf
- [3] LangGraph Studio Guide: Installation, Set Up, Use Cases: https://www.datacamp.com/tutorial/langgraph-studio
- [4] Is Autogen Worth the Hype? Limitations and Real-World Use Cases Revealed: https://www.toolify.ai/ai-news/is-autogen-worth-the-hype-limitations-and-realworld-use-cases-revealed-1482386
- [5] Exploring AutoGen: The Future of AI-Assisted Conversations and ... - Medium: https://medium.com/@kofsitho/exploring-autogen-the-future-of-ai-assisted-conversations-and-automation-2763f10615f6


    ## Conclusion

In this report, we have explored the distinct features, use cases, and limitations of LangGraph and AutoGen, two powerful frameworks for building applications with large language models (LLMs). Each framework offers unique capabilities that cater to different needs, making them suitable for various applications in the AI landscape.

LangGraph stands out with its robust state management and dynamic tools integration, making it ideal for stateful, multi-actor applications. Its support for cycles, controllability, and persistence allows for flexible and complex workflows, which are essential for agentic architectures. LangGraph's streaming capabilities further enhance its suitability for production applications that require simultaneous processing of multiple conversations. However, its focus on language tasks and the complexity of its setup may limit its applicability in broader AI domains.

AutoGen, developed by Microsoft, emphasizes multi-agent collaboration and automation. Its features, such as code generation and execution, human proxy agent, and a user-friendly graphical interface, make it a strong contender for applications requiring advanced problem-solving and collaborative multi-agent systems. AutoGen's community-driven development fosters continuous innovation, although its high operational costs and incompatibility with open-source models pose challenges for extensive use.

The use cases for each framework highlight their strengths: LangGraph excels in conversational agents, long-running applications, and human-in-the-loop interactions, while AutoGen is well-suited for sophisticated problem-solving, collaborative systems, and industries like automotive and manufacturing. Despite their limitations, both frameworks offer valuable tools for AI agent development, with LangGraph focusing on language tasks and AutoGen on multi-agent orchestration.

In summary, the choice between LangGraph and AutoGen depends on the specific requirements of the application, including the need for state management, multi-agent collaboration, and the balance between cost and functionality. By understanding their unique features and limitations, developers can make informed decisions to leverage the strengths of each framework effectively."""

def create_custom_styles():
    """Create custom styles for different text elements with improved formatting"""
    styles = getSampleStyleSheet()
    
    # Add styles only if they don't exist
    if 'CustomTitle' not in styles:
        styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#2C3E50'),
            alignment=1  # Center alignment
        ))
    
    if 'CustomHeading1' not in styles:
        styles.add(ParagraphStyle(
            name='CustomHeading1',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=16,
            spaceBefore=24,
            textColor=colors.HexColor('#2C3E50')
        ))
    
    if 'CustomHeading2' not in styles:
        styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.HexColor('#34495E')
        ))
    
    if 'CustomHeading3' not in styles:
        styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=styles['Heading3'],
            fontSize=14,
            spaceAfter=10,
            spaceBefore=16,
            textColor=colors.HexColor('#34495E')
        ))
    
    if 'CustomNormal' not in styles:
        styles.add(ParagraphStyle(
            name='CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceBefore=8,
            spaceAfter=8,
            textColor=colors.HexColor('#2C3E50'),
            leading=16
        ))
    
    if 'BulletList' not in styles:
        styles.add(ParagraphStyle(
            name='BulletList',
            parent=styles['Normal'],
            fontSize=11,
            leftIndent=36,
            spaceBefore=8,
            spaceAfter=8,
            bulletIndent=20,
            leading=16,
            textColor=colors.HexColor('#2C3E50')
        ))
    
    if 'NestedBulletList' not in styles:
        styles.add(ParagraphStyle(
            name='NestedBulletList',
            parent=styles['BulletList'],
            leftIndent=56,
            bulletIndent=40
        ))
    
    if 'Citation' not in styles:
        styles.add(ParagraphStyle(
            name='Citation',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#666666'),
            super=True
        ))
    
    if 'TableCell' not in styles:
        styles.add(ParagraphStyle(
            name='TableCell',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            spaceBefore=6,
            spaceAfter=6,
            textColor=colors.HexColor('#2C3E50')
        ))
    if 'References' not in styles:
        styles.add(ParagraphStyle(
            name='References',
            parent=styles['Normal'],
            fontSize=9,        # Smaller text
            leading=11,       # Tighter line spacing
            spaceBefore=1,    # Minimal space before
            spaceAfter=1,     # Minimal space after
            textColor=colors.HexColor('#2C3E50')
        ))
    return styles


def wrap_text_in_cell(text, style):
    """Wrap text in a cell using Paragraph"""
    return Paragraph(text, style)

def process_table_html(table_html, styles):
    """Process HTML tables with improved formatting and modern styling"""
    soup = BeautifulSoup(table_html, 'html.parser')
    data = []
    
    # Get headers with white text color explicitly set in the HTML
    headers = []
    header_row = soup.find('tr')
    if header_row:
        for th in header_row.find_all(['th', 'td']):
            # Add white color to header text explicitly in the HTML
            header_text = f'<b><font color="white">{th.text.strip()}</font></b>'
            headers.append(wrap_text_in_cell(header_text, styles['TableCell']))
        data.append(headers)
    
    # Get rows (remaining code unchanged)
    for row in soup.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            row_data = []
            for col in cols:
                row_data.append(wrap_text_in_cell(col.text.strip(), styles['TableCell']))
            data.append(row_data)
    
    if not data:
        return None
    
    # Calculate column widths - make first column slightly wider
    available_width = 450
    num_cols = len(data[0])
    if num_cols > 1:
        first_col_width = available_width * 0.3  # 30% for first column
        remaining_width = available_width - first_col_width
        other_col_widths = remaining_width / (num_cols - 1)
        col_widths = [first_col_width] + [other_col_widths] * (num_cols - 1)
    else:
        col_widths = [available_width]
    
    # Enhanced modern table style (unchanged)
    style = TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),  # Dark blue header
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Zebra striping for rows
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2C3E50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        
        # Alternate row colors
        *[('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F8F9FA')) 
          for i in range(2, len(data), 2)],  # Light gray for alternate rows
        
        # Subtle grid styling
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E0E0E0')),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#2C3E50')),  # Thicker header bottom line
        
        # First column styling
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F4F6F6')),  # Light gray for first column
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        
        # Rounded corners
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
    ])
    
    # Add padding around the table
    table = Table(data, colWidths=col_widths, style=style, spaceBefore=12, spaceAfter=12)
    return table

def process_list_items(list_element, styles, style_name='BulletList'):
    """Process list items with improved bullet points and spacing"""
    items = []
    for item in list_element.find_all('li', recursive=False):
        # Handle nested lists
        nested_lists = item.find_all(['ul', 'ol'], recursive=False)
        
        # Get the raw HTML content of the list item
        item_html = str(item)
        
        # Process text while preserving HTML formatting
        # Remove the outer <li> tags to get just the content
        text = item_html.replace('<li>', '', 1)
        if text.endswith('</li>'):
            text = text[:-5]
            
        # Convert markdown-style bold to HTML bold
        text = text.replace('**', '<b>')  # First occurrence becomes opening tag
        text = text.replace('**', '</b>', 1)  # Second occurrence becomes closing tag
        
        # Add custom bullet point
        bullet = '• ' if list_element.name == 'ul' else f"{len(items)+1}. "
        
        # Handle citations with superscript
        text = text.replace('[', '<super><font color="#666666">[').replace(']', ']</font></super>')
        
        para = Paragraph(f"{bullet}{text}", styles[style_name])
        items.append(para)
        items.append(Spacer(1, 4))  # Add spacing between list items
        
        # Process nested lists
        for nested_list in nested_lists:
            items.extend(process_list_items(nested_list, styles, 'NestedBulletList'))
    
    return items

def markdown_to_pdf_enhanced(markdown_text, output_filename):
    """Convert markdown to PDF with enhanced formatting and styling"""
    html = markdown(markdown_text, extensions=['tables', 'fenced_code', 'def_list'])
    soup = BeautifulSoup(html, 'html.parser')
    
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = create_custom_styles()
    story = []
    
    # Track if we're in a sources section
    in_sources = False
    
    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'table', 'ul', 'ol', 'pre']):
        # Check if we're entering or leaving sources section
        if element.name in ['h1', 'h2', 'h3']:
            if 'Sources' in element.get_text():
                in_sources = True
            else:
                in_sources = False
        
        # Handle lists
        if element.name in ['ul', 'ol']:
            style_name = 'References' if in_sources else 'BulletList'
            list_items = process_list_items(element, styles, style_name)
            story.extend(list_items)
            if not in_sources:  # Only add extra spacing if not in sources
                story.append(Spacer(1, 6))
        
        # Handle code blocks    
        elif element.name == 'pre':
            code_style = ParagraphStyle(
                'Code',
                parent=styles['Normal'],
                fontName='Courier',
                fontSize=9,
                leading=12,
                leftIndent=36,
                rightIndent=36,
                spaceBefore=12,
                spaceAfter=12,
                backColor=colors.white
            )
            code_text = element.get_text()
            story.append(Paragraph(code_text, code_style))
        
        # Handle tables    
        elif element.name == 'table':
            table = process_table_html(str(element), styles)
            if table:
                story.append(Spacer(1, 12))
                story.append(table)
                story.append(Spacer(1, 12))
        
        # Handle paragraphs and headers
        else:
            # Check if this is a reference by looking for common patterns
            is_reference = False
            text = element.get_text().strip()
            
            # Pattern 1: Starts with [number]
            if text.startswith('[') and ']' in text:
                bracket_content = text[1:text.find(']')]
                if bracket_content.isdigit():  # Checks if the content between brackets is a number
                    is_reference = True
            
            # Pattern 2: Contains a URL
            if any(url_pattern in text.lower() for url_pattern in ['http://', 'https://', 'www.']):
                is_reference = True
            
            if is_reference and element.name == 'p':  # Only apply reference styling to paragraphs
                # Format reference number as superscript
                text = text.replace('[', '<super>[').replace(']', ']</super>', 1)
                
                # Make URLs gray and italic
                for url_pattern in ['http://', 'https://', 'www.']:
                    if url_pattern in text.lower():
                        url_start = text.lower().find(url_pattern)
                        # Find the end of the URL (space or end of string)
                        url_end = text.find(' ', url_start) if text.find(' ', url_start) != -1 else len(text)
                        url = text[url_start:url_end]
                        text = text[:url_start] + f'<font color="#666666"><i>{url}</i></font>' + text[url_end:]
                
                # Use References style for reference paragraphs
                para = Paragraph(text, styles['References'])
                story.append(para)
            
            else:
                # Handle regular paragraphs and headers
                style_name = {
                    'h1': 'CustomHeading1',
                    'h2': 'CustomHeading2',
                    'h3': 'CustomHeading3',
                    'p': 'CustomNormal'
                }.get(element.name, 'CustomNormal')
                
                # Handle inline formatting
                content = str(element)
                content = content.replace('<strong>', '<b>').replace('</strong>', '</b>')
                content = content.replace('<em>', '<i>').replace('</em>', '</i>')
                
                # Create paragraph with appropriate style
                para = Paragraph(content, styles[style_name])
                story.append(para)
                
                # Add space after headings
                if element.name in ['h1', 'h2', 'h3']:
                    story.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(story)

if __name__ == "__main__":

    
    markdown_to_pdf_enhanced(report, "D:/data/reports/test_output.pdf")