# Multi-Agent Research System

A powerful multi-agent research pipeline built with LangChain that automates topic discovery, content extraction, report generation, and quality evaluation. This repository is designed for research workflows where reliable web search, structured content scraping, and summarized output are required.

## Overview

This project uses multiple specialized agents working together to handle different stages of research:

- Search for relevant articles with a web search agent
- Scrape and parse content from discovered URLs
- Generate a structured research report
- Evaluate the report with a critic chain

The result is a single consolidated report plus actionable critique and score annotations.

## Key Features

- **Automated topic research** with query-driven web search
- **Content scraping** from web pages using BeautifulSoup
- **Structured report generation** using LangChain and LLM prompts
- **Quality evaluation** via a critic chain that scores and improves output
- **CLI and Streamlit UI support** for flexible usage
- **Modular design** for custom extensions and new agent chains

## Architecture

This diagram summarizes the pipeline flow:

```text
User input: research topic
       │
       ▼
Search Agent (Tavily API)
       │
       ▼
Reader Agent (BeautifulSoup scraping)
       │
       ▼
Writer Chain (report generation)
       │
       ▼
Critic Chain (feedback + scoring)
       │
       ▼
Final report + critic output
```

## Requirements

- Python 3.13+
- `pip` package manager
- `streamlit` for the web UI
- API keys for Tavily and OpenRouter

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-org>/multi_agent_system.git
cd multi_agent_system
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux / macOS
```

3. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root containing the required API keys:

```env
TAVILY_API_KEY=your_tavily_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
# Optional: OPENAI_API_KEY=your_openai_key
```

If you want to use OpenAI instead of OpenRouter, add `OPENAI_API_KEY` and configure the environment accordingly.

## Usage

### Run the research pipeline from CLI

```bash
python pipeline.py
```

The CLI asks for a research topic and displays the generated report and critic feedback.

### Run the Streamlit web UI

```bash
streamlit run app.py
```

Open the local URL shown in your browser. Use the web interface to enter a topic and view the generated output.

## Example Workflow

1. Start the app or run `python pipeline.py`
2. Enter a topic such as "sustainable energy transition" or "AI in healthcare"
3. The search agent finds recent articles and URLs
4. The reader agent scrapes page content and extracts relevant text
5. The writer chain compiles a structured summary report
6. The critic chain evaluates the report and provides score-based feedback

## Project Structure

| File | Purpose |
|------|---------|
| `agents.py` | Defines the agents, tools, and LangChain pipeline behavior |
| `tools.py` | Implements search and scraping utilities used by agents |
| `pipeline.py` | Orchestrates the full research workflow and report generation |
| `app.py` | Builds a Streamlit web UI for the pipeline |
| `main.py` | Entrypoint for command-line execution and startup logic |
| `requirements.txt` | Project dependencies |
| `pyproject.toml` | Package metadata and tooling configuration |

## Components

### `tools.py`
- `web_search` — searches the web via Tavily and returns a list of candidate URLs and metadata
- `scrape_url` — fetches web pages and extracts plaintext content with BeautifulSoup

### `agents.py`
- Agent definitions and chain composition using LangChain
- LCEL-based writer and critic chains for report generation and evaluation

### `pipeline.py`
- High-level orchestration for end-to-end research execution
- Integrates web search, scraping, writing, and critic evaluation

### `app.py`
- Streamlit app for interactive user input
- Displays generated report and critic output in a simple web interface

## Notes

- Ensure your `.env` file keys are valid before running the app.
- The report quality depends on search results and the chosen LLM provider.
- Scraping may fail for pages that block bots or require JavaScript rendering.

## Extending This Project

You can extend the system by:

- Adding new tools for domain-specific data sources
- Improving the prompt templates in the writer and critic chains
- Adding caching or browser-based scraping for JS-heavy websites
- Supporting additional LLM providers or local models

## Troubleshooting

- If the search agent returns no results, verify `TAVILY_API_KEY` and endpoint availability.
- If scraping fails, check the target URL and whether the site blocks automated requests.
- If LLM responses are missing or malformed, confirm `OPENROUTER_API_KEY` and model settings.

## License

MIT
