from autogen_agentchat.agents import AssistantAgent 
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os 
import arxiv 
from typing import List, Dict, AsyncGenerator



def arxiv_search(query: str, max_results: int = 5) -> List[Dict]:
    """Return a compact list of arxiv papers matching *query*.
    Each element contains: `title`, `authors`,`published`, `summary` and
    `pdf_url`. The helper is wrapped as an Autogen *FunctionTool* below so it
    can be invoked by agents through the normal tool-use mechanism.  
    """

    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    papers: List[Dict] = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "published": result.published.strftime("%Y-%m-%d"),
            "summary": result.summary,
            "pdf_url": result.pdf_url,
        })
    return papers

print(arxiv_search(query='agents'))