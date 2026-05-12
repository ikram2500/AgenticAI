# arXiv Research Assistant - Project Documentation

## Overview

The **arXiv Research Assistant** is an intelligent multi-agent system designed to automate academic literature reviews. Built on Microsoft's AutoGen framework, it leverages a team of specialized AI agents to search arXiv, retrieve relevant papers, and generate comprehensive literature review reports — all through an intuitive web interface.

This project demonstrates the power of agentic AI systems for research automation, serving as a production-ready reference implementation for organizations seeking to accelerate academic research workflows.

---

## Key Features

- **Multi-Agent Architecture**: Two specialized AI agents collaborate — one searches arXiv, another synthesizes findings
- **Streamlit Web Interface**: User-friendly UI for entering research topics and configuring parameters
- **Automated Literature Review**: Generates structured markdown reports with paper summaries, key contributions, and insights
- **PDF Download**: Export literature reviews in markdown format for immediate use
- **Configurable Parameters**: Adjust the number of papers to retrieve (1-10)
- **API Key Management**: Secure sidebar interface for OpenAI API key configuration

---

## Architecture

### Agent System Design

The system employs a **Round-Robin Group Chat** pattern with two agents:

| Agent | Role | Responsibility |
|-------|------|----------------|
| **arxiv_researcher_agent** | Search Specialist | Formulates optimal arXiv queries, invokes the search tool, selects relevant papers |
| **arxiv_summarizer_agent** | Content Synthesizer | Receives paper data, writes literature review with introduction, bullet summaries, and takeaways |

### Data Flow

```
User Input (Topic, # Papers)
         ↓
arxiv_researcher_agent
  ↓ (generates query)
arxiv_search() function (tool)
  ↓ (retrieves papers)
arxiv_researcher_agent
  ↓ (selects papers, formats as JSON)
arxiv_summarizer_agent
  ↓ (generates markdown report)
Literature Review Output
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Agent Framework** | Microsoft AutoGen | Multi-agent orchestration, tool use |
| **LLM Backend** | OpenAI GPT-4o | Reasoning and content generation |
| **Web Framework** | Streamlit | Interactive UI |
| **Paper Database** | arXiv API | Academic paper retrieval |
| **Python Runtime** | Python 3.10+ | Core application logic |

---

## Project Structure

```
arxiv_autogen_paper_finder/
├── app.py                 # Streamlit web application (main entry point)
├── agent-be.py            # CLI-based agent implementation
├── check_arxiv.py         # Standalone arXiv search utility
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── venv/                  # Python virtual environment
```

### File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application with UI, agent initialization, and research pipeline |
| `agent-be.py` | Alternative CLI version demonstrating programmatic agent usage |
| `check_arxiv.py` | Standalone script for testing arXiv API connectivity |
| `requirements.txt` | Lists all required Python packages with versions |

---

## Installation & Setup

### Prerequisites

- Python 3.10 or higher
- OpenAI API key (GPT-4o access required)

### Setup Steps

1. **Clone or copy the project directory**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your OpenAI API key**
   - Option A: Create a `.env` file with `OPENAI_API_KEY=your_key`
   - Option B: Enter it in the web interface sidebar at runtime

6. **Launch the application**
   ```bash
   streamlit run app.py
   ```

---

## Usage Guide

### Running the Web Application

1. Execute `streamlit run app.py`
2. Enter your OpenAI API key in the sidebar
3. Type your research topic (e.g., "transformer architecture in computer vision")
4. Adjust the number of papers using the slider (1-10)
5. Click **"Generate Literature Review"**
6. Review the generated report
7. Click **"Download Report"** to save as a markdown file

### Example Output

The system generates a literature review containing:

- **Introduction**: 2-3 sentence overview of the research topic
- **Paper Summaries**: Bullet points with title (linked to PDF), authors, problem tackled, and key contributions
- **Takeaway**: Single-sentence synthesis of the research landscape

---

## Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| OpenAI API Key | Authentication for GPT-4o | User-provided |
| Research Topic | Subject area for paper search | User-provided |
| Number of Papers | How many papers to retrieve | 3 |

---

## Security Considerations

- API keys are never stored or persisted — entered per session
- No data leaves the user's environment except API calls to OpenAI
- The virtual environment (`venv/`) should not be committed to version control

---

## Extensibility

This project serves as a foundation for more advanced implementations:

- **Expand agent capabilities**: Add more agents for specialized tasks (e.g., citation analysis, comparison synthesis)
- **Integrate additional sources**: Connect to Semantic Scholar, PubMed, or Google Scholar
- **Add persistent storage**: Implement database for saving research sessions
- **Enhance reporting**: Generate formatted PDFs, slide decks, or LaTeX documents

---

## Dependencies

```
autogen-agentchat   # AutoGen multi-agent framework
autogen-core        # Core agent infrastructure
autogen-ext         # Extended utilities
streamlit           # Web UI framework
arxiv               # arXiv API client
dotenv              # Environment variable management
tiktoken            # Tokenization for API optimization
openai              # OpenAI API client
```

---

## Support & Maintenance

For questions, enhancements, or custom integrations, contact the development team.

---

*This project demonstrates enterprise-ready AI agent implementation using Microsoft's AutoGen framework and can be customized to meet specific organizational research automation needs.*