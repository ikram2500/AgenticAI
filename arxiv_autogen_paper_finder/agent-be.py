from autogen_agentchat.agents import AssistantAgent 
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os 
import asyncio
from autogen_agentchat.teams import RoundRobinGroupChat
import arxiv 
from typing import List, Dict, AsyncGenerator

openai_brain = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY", ""),
)

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

arxiv_researcher_agent = AssistantAgent(
    name = "arxiv_researcher_agent",
    description = "Create arxiv queries and rerieves candidates papers.",
    model_client= openai_brain,
    tools = [arxiv_search],
    system_message=(
        "Given a user topic, think of the best arxiv query. "
        "When the tool returns, choose exactly the number of papers requested and pass "
        "them as concise JSON to the summarizer."
        ),

)



summarizer_agent  = AssistantAgent(
    name = "arxiv_summarizer_agent",
    description = "An agent that summarizes arxiv papers.",
    model_client= openai_brain,
    system_message = (
        "You are an expert researcher. when you receive the JSON list of"
        "paers, write a literature review style report in Markdown:\n" \
        "1. Start with a 2-3 sentence introduction to the topic.\n " \
        "2. Then include one bullet per paper with: title (as Markdow link), "
        "authors, the specific problem tackled, and its key "
         "contribution. \n" \
        "3. Close with a single-sentence takeaway"   
        ),
    
)

team = RoundRobinGroupChat(
    participants = [arxiv_researcher_agent, summarizer_agent],
    max_turns=2,
)

async def run_team():

    task = 'Conduct a literature review on the topic - Autogen and return exactly 3 papers'

    async for msg in team.run_stream(task = task):
        print(msg)

if __name__ == "__main__":
    asyncio.run(run_team())


# test code to run the agent
"""from autogen_core.models import UserMessage
import asyncio

async def main():
    result = await openai_brain.create([UserMessage(content="What is the capital of France?", source="user")])
    print(result)
    await openai_brain.close()

asyncio.run(main())"""
