# Multi-Agent Research System

A powerful multi-agent research pipeline built with LangChain that automates the research process through specialized agents. The system takes a research topic and generates a comprehensive, structured report with quality evaluation.

## Features

- **Web Search Agent** - Uses Tavily API to find recent, relevant information
- **Content Reader Agent** - Scrapes and extracts detailed content from URLs using BeautifulSoup
- **Report Writer Chain** - Generates professional, structured research reports
- **Critic Chain** - Evaluates reports with scores and actionable feedback
- **Dual Interfaces** - CLI and Streamlit web UI

## Architecture

```
User Input (topic)
       │
       ▼
┌─────────────────────────────┐
│   Search Agent              │
│   (Tavily API)              │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│   Reader Agent              │
│   (BeautifulSoup)           │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│   Writer Chain (LCEL)      │
│   Report Generation        │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│   Critic Chain (LCEL)      │
│   Quality Evaluation        │
└─────────────────────────────┘
       │
       ▼
    Final Report + Feedback
```

## Installation

```bash
# Clone the repository
cd multi_agent_system

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
# Optional: OPENAI_API_KEY=your_openai_key
```

Get your API keys:
- [Tavily](https://tavily.com/) - Search API
- [OpenRouter](https://openrouter.ai/) - LLM API (free tier available)

## Usage

### Command Line

```bash
python pipeline.py
```

### Streamlit Web UI

```bash
streamlit run app.py
```

## Project Structure

| File | Description |
|------|-------------|
| `tools.py` | Tool definitions (web_search, scrape_url) |
| `agents.py` | Agent and LCEL chain definitions |
| `pipeline.py` | Core research pipeline orchestration |
| `app.py` | Streamlit web interface |
| `main.py` | Entry point |
| `requirements.txt` | Python dependencies |

## Tech Stack

- **LangChain** - Agent framework and LCEL chains
- **OpenRouter** - LLM API (gpt-oss-20b:free model)
- **Tavily** - Web search
- **BeautifulSoup** - Web scraping
- **Streamlit** - Web UI
- **Python 3.13+**

## License

MIT