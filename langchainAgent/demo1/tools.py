from duckduckgo_search import DDGS
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun 
from langchain_community.utilities import WikipediaAPIWrapper 
from langchain_core.tools import tool
from datetime import datetime 

@tool
def search(query: str) -> str:
    """Search the web for information."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        return str(list(results))
    
@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for information."""
    api_wraper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
    wiki_tool = WikipediaQueryRun(api_wrapper=api_wraper)
    return wiki_tool.run(query)