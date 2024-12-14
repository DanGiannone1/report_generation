
from markdown import markdown
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak



report = """# LangGraph vs CrewAI: A Comparative Analysis

## Introduction

In the rapidly evolving landscape of artificial intelligence, the development of multi-agent systems has become a focal point for enhancing the capabilities of AI applications. Two prominent frameworks, LangGraph and CrewAI, have emerged as leaders in this domain, each offering unique features and catering to distinct use cases. This report delves into a detailed comparison of LangGraph and CrewAI, examining their features, use cases, and limitations to provide a comprehensive understanding of their respective strengths and weaknesses.

LangGraph is a library specifically designed for building stateful, multi-actor applications with Large Language Models (LLMs). It extends the LangChain library, offering a robust framework for orchestrating complex workflows. Key features of LangGraph include its ability to handle multi-agent workflows with advanced loops and if-statements, support for cyclic graphs, sophisticated state management, multi-language support, and seamless integration with external tools and APIs. These features make LangGraph particularly suitable for applications requiring complex language processing tasks and dynamic simulation environments.

On the other hand, CrewAI is an open-source framework that focuses on streamlining AI agent management, especially in collaborative settings. Developed in Python, CrewAI emphasizes task automation and agent collaboration, making it ideal for production environments. Its key features include task automation, structured orchestration of collaborative AI agent teams, a role-based design for managing interactions, and integration with LangChain for developers familiar with the framework. CrewAI's production orientation and practical usability make it a preferred choice for real-world applications in various industries.

The report further explores the distinct use cases for each framework. LangGraph excels in developing conversational agents, long-running multi-step applications, and complex workflow management, leveraging its stateful interactions with LLMs. Conversely, CrewAI is tailored for AI automation in business processes, multi-agent collaboration, and real-world applications, providing a flexible framework for orchestrating autonomous AI agents.

Despite their strengths, both LangGraph and CrewAI have limitations. LangGraph's focus on language tasks restricts its versatility, while CrewAI's automation capabilities come with brittleness and limited error tolerance. Additionally, CrewAI faces challenges in handling complex workflows and has limitations in deployment and integration options.

This report aims to equip developers and AI practitioners with the insights needed to choose the most suitable framework for their specific needs, balancing the strengths and limitations of LangGraph and CrewAI.
    ## Features

**LangGraph and CrewAI both offer robust frameworks for building multi-agent AI systems, but they excel in different areas, catering to distinct use cases and technical requirements.**

### LangGraph Features

LangGraph is a library designed for building stateful, multi-actor applications with Large Language Models (LLMs). It extends the LangChain library, providing a comprehensive framework for orchestrating complex workflows. Key features include:

- **Multi-Agent Workflows**: LangGraph enables the development of advanced workflows with multiple loops and if-statements, making it suitable for creating both agent and multi-agent workflows [1][2].
- **Cyclic Graphs**: It represents workflows as cyclical graphs, allowing developers to orchestrate interactions of multiple LLM agents efficiently [3].
- **State Management**: LangGraph supports sophisticated state management, maintaining information across multiple steps of computation [4].
- **Multi-Language Support**: It offers robust support for multiple languages, making it ideal for complex language processing tasks such as translation and sentiment analysis [5].
- **Integration with External Tools**: LangGraph allows for the connection to external tools and APIs, enhancing its flexibility in handling diverse tasks [3].

### CrewAI Features

CrewAI is an open-source framework focused on streamlining AI agent management, particularly in collaborative environments. It is developed in Python and emphasizes task automation and agent collaboration. Key features include:

- **Task Automation**: CrewAI automates task distribution and resource management, allowing agents to focus on their specific roles with minimal manual intervention [6].
- **Structured Orchestration**: It excels in orchestrating collaborative AI agent teams, enabling efficient execution of complex workflows [7].
- **Role-Based Design**: CrewAI uses a structured role-based design to manage interactions among multiple agents, simulating human-like teamwork [8].
- **Production Orientation**: Tailored for production environments, CrewAI emphasizes well-structured code and practical usability [9].     
- **Integration with LangChain**: For developers familiar with LangChain, CrewAI offers straightforward integration of existing solo agents into its framework [10].

### Comparison Table

| Feature                  | LangGraph                                      | CrewAI                                      |
|--------------------------|------------------------------------------------|---------------------------------------------|
| Multi-Agent Workflows    | Advanced workflows with loops and if-statements| Collaborative agent teams                   |
| State Management         | Sophisticated state management                 | Role-based design for teamwork              |
| Language Support         | Multi-language support                         | Focus on task automation                    |
| Integration              | Connects to external tools and APIs            | Integrates with LangChain                   |
| Production Orientation   | Not specified                                  | Tailored for production environments        |

### Sources

- From Basics to Advanced: Exploring LangGraph: https://towardsdatascience.com/from-basics-to-advanced-exploring-langgraph-e8c1cf4db787     
- LangGraph - GitHub Pages: https://langchain-ai.github.io/langgraph/
- LangGraph Tutorial: A Comprehensive Guide for Beginners: https://blog.futuresmart.ai/langgraph-tutorial-for-beginners
- LangGraph: A Beginner's Guide to Building AI Workflows: https://medium.com/@gopiariv/langgraph-a-beginners-guide-to-building-ai-workflows-e500965f2ef9
- CrewAI vs Autogen vs Langgraph: https://medium.com/@isaac.casm/crewai-vs-autogen-vs-langgraph-c5d9c44f7520
- Unlocking the Power of AI with CrewAI: A Comprehensive Overview: https://www.squareshift.co/post/unlocking-the-power-of-ai-with-crewai-a-comprehensive-overview
- Building AI Agents with CrewAI: A Step-by-Step Guide: https://medium.com/@sahin.samia/building-ai-agents-with-crewai-a-step-by-step-guide-172627e110c5
- Understanding CrewAI: A Deep Dive into Multi-Agent AI Systems: https://medium.com/accredian/understanding-crewai-a-deep-dive-into-multi-agent-ai-systems-110d04703454
- Comparing Multi-agent AI frameworks: CrewAI, LangGraph ... - Concision: https://www.concision.ai/blog/comparing-multi-agent-ai-frameworks-crewai-langgraph-autogpt-autogen
- Langgraph Vs Crewai Comparison - Restackio: https://www.restack.io/p/multi-agents-answer-langgraph-vs-crewai-cat-ai

## Use Cases

**LangGraph and CrewAI serve distinct yet overlapping use cases, each excelling in different areas of AI application development.**

LangGraph is particularly well-suited for applications that require stateful, multi-actor interactions with large language models (LLMs). Its primary use cases include:

- **Conversational Agents**: LangGraph is ideal for developing chatbots that can handle complex dialogues and require persistent state management. This is due to its ability to manage non-linear, cyclic workflows, which are essential for adaptive learning systems and dynamic simulation environments [1][2].
- **Long-running, Multi-step Applications**: LangGraph excels in scenarios where applications need to perform complex tasks over extended periods, benefiting from its support for persistent checkpoints and human-in-the-loop interactions [3].
- **Complex Workflow Management**: It is effective in managing workflows that involve multiple agents or tasks, leveraging LLMs for tasks like content generation, summarization, and translation [4].

CrewAI, on the other hand, is designed for environments that require production-grade applications with a focus on task distribution and practical usability. Its key use cases include:

- **AI Automation in Business Processes**: CrewAI is used extensively in automating workflows across various domains such as finance, healthcare, and marketing. It streamlines processes like lead scoring, content production, and strategic planning by utilizing AI-driven agents [5][6].
- **Multi-Agent Collaboration**: CrewAI provides a flexible framework for orchestrating autonomous AI agents, making it suitable for applications like smart assistants and customer service teams [7].
- **Real-World Applications**: CrewAI is tailored for practical applications in industry, such as automated project planning systems, lead-scoring, and engagement automation [8].

### Sources

- LangGraph Tutorial: What Is LangGraph and How to Use It? : https://www.datacamp.com/tutorial/langgraph-tutorial
- A Quick Introduction to LangGraph: Enhancing LLM Applications ... - Medium : https://becomingahacker.org/a-quick-introduction-to-langgraph-enhancing-llm-applications-with-cyclic-workflows-145f61f38747
- Source GitHub - langchain-ai/langgraph-example : https://github.com/langchain-ai/langgraph-example
- Optimizing Workflow Efficiency with LangGraph and Agents: Key ... - Medium : https://medium.com/@abhilashkrish/optimizing-workflow-efficiency-with-langgraph-and-agents-key-features-use-cases-and-integration-6c9ae3d7f502
- CrewAI Examples - CrewAI : https://docs.crewai.com/examples/example
- Use Cases - crewai.com : https://www.crewai.com/use-cases
- Guide to CrewAI: Autonomous AI Collaboration - Devzery Latest : https://www.devzery.com/post/guide-to-crewai
- Practical multi AI agents and advanced use cases with crew AI : https://github.com/64FC/DeepLearningAI_Practical_Multi_AI_Agents_CrewAI/blob/main/README.md

## Limitations

**LangGraph and CrewAI, while both powerful multi-agent frameworks, have distinct limitations that impact their usability and application scope.**

### LangGraph Limitations

1. **Focused Task Limitation**: LangGraph is highly specialized for language tasks, which means it may not be suitable for projects requiring broader AI capabilities, such as computer vision or predictive analytics [1].
2. **Complexity in Visualization**: Although LangGraph excels in visualizing task interdependencies through its graph-based approach, this can also become a limitation when dealing with overly complex graphs, potentially leading to difficulties in managing and interpreting the data [2].
3. **Limited Scope**: Its focus on language tasks restricts its application to areas like text analysis, translation, and sentiment analysis, limiting its versatility in other AI domains [3].

### CrewAI Limitations

1. **Brittleness and Error Tolerance**: CrewAI's automation capabilities are powerful, but they come with brittleness and limited error tolerance, necessitating careful management and proactive strategies to mitigate these issues [4].
2. **Complex Workflow Challenges**: While effective for straightforward tasks, CrewAI may struggle with complex workflows that require multiple agents working dynamically across varied scenarios [5].
3. **Deployment and Integration Limitations**: CrewAI has limitations in its deployment options and integration ecosystems, which can impact its accessibility and enterprise readiness compared to more comprehensive platforms [6].

### Comparative Summary

| Feature/Aspect            | LangGraph Limitations                                    | CrewAI Limitations                                 
     |
|---------------------------|----------------------------------------------------------|---------------------------------------------------------|
| Task Specialization       | Focused on language tasks, limiting broader AI use cases | Effective for straightforward tasks, struggles with complex workflows |
| Error Management          | N/A                                                      | Brittleness and limited error tolerance            
      |
| Deployment and Integration| N/A                                                      | Limited deployment options and integration ecosystems    |

### Sources

- Comparing Multi-agent AI frameworks: CrewAI, LangGraph ... - Concision: https://www.concision.ai/blog/comparing-multi-agent-ai-frameworks-crewai-langgraph-autogpt-autogen
- LangGraph: Challenges as a Multi-Agent Orchestrator?: https://medium.com/@shubham.shardul2019/is-langgraph-the-ultimate-multi-agent-maestro-explore-its-potential-and-hidden-hurdles-c7e454a3e089
- CrewAI vs Autogen vs Langgraph. When I first used ChatGPT, I ... - Medium: https://medium.com/@isaac.casm/crewai-vs-autogen-vs-langgraph-c5d9c44f7520
- How to Automate Processes with CrewAI - Stephen Collins.tech: https://stephencollins.tech/posts/how-to-automate-processes-with-crewai     
- CrewAI vs. MetaGPT: Comparing Open-Source AI Frameworks: https://smythos.com/ai-agents/ai-agent-builders/crewai-vs-metagpt-2/
- Discover how CrewAI vs. MetaGPT stack up in AI collaboration: https://smythos.com/ai-agents/ai-agent-builders/crewai-vs-metagpt/


    ## Conclusion

In comparing LangGraph and CrewAI, it is evident that both frameworks offer unique strengths and cater to different needs within the realm of multi-agent AI systems. LangGraph stands out with its robust framework for building stateful, multi-actor applications, particularly excelling in complex language processing tasks. Its ability to manage multi-agent workflows through cyclic graphs and sophisticated state management makes it ideal for applications requiring persistent state management and complex workflow orchestration. However, its specialization in language tasks limits its versatility in broader AI domains.

CrewAI, on the other hand, is tailored for production environments, emphasizing task automation and agent collaboration. Its structured role-based design and focus on practical usability make it a strong candidate for automating business processes and orchestrating collaborative AI agent teams. Despite its strengths, CrewAI faces challenges with complex workflows and has limitations in deployment options and integration ecosystems, which can impact its enterprise readiness.

The use cases for each framework further highlight their distinct applications. LangGraph is well-suited for conversational agents and long-running, multi-step applications, leveraging its capabilities in managing complex workflows. CrewAI excels in AI automation within business processes and multi-agent collaboration, making it suitable for real-world applications like smart assistants and customer service teams.   

Both frameworks have their limitations. LangGraph's focus on language tasks restricts its application scope, while CrewAI's brittleness and limited error tolerance require careful management. These limitations underscore the importance of selecting the right framework based on specific project requirements and technical needs.

In summary, the choice between LangGraph and CrewAI should be guided by the specific demands of the project at hand. LangGraph is ideal for language-centric applications requiring complex workflow management, while CrewAI is better suited for production-grade environments needing efficient task automation and agent collaboration. Understanding these nuances will enable developers to leverage the strengths of each framework effectively, ensuring successful implementation of multi-agent AI systems.
"""

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