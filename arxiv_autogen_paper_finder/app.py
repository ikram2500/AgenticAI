import streamlit as st
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
import asyncio
from autogen_agentchat.teams import RoundRobinGroupChat
import arxiv
from typing import List, Dict

st.set_page_config(page_title="arXiv Research Assistant", page_icon="📚")

st.title("📚 arXiv Literature Review Assistant")
st.markdown("Enter a research topic and let AI agents find and summarize relevant papers from arXiv.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "result" not in st.session_state:
    st.session_state.result = None

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

topic = st.text_input("Research Topic", placeholder="e.g., Autogen multi-agent systems", value=st.session_state.get("topic", ""))
num_papers = st.slider("Number of papers", 1, 10, 3)

def arxiv_search(query: str, max_results: int = 2) -> List[Dict]:
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

def create_team(api_key: str):
    openai_brain = OpenAIChatCompletionClient(model="gpt-4o", api_key=api_key)

    arxiv_researcher_agent = AssistantAgent(
        name="arxiv_researcher_agent",
        description="Create arxiv queries and retrieves candidate papers.",
        model_client=openai_brain,
        tools=[arxiv_search],
        system_message=(
            "Given a user topic, think of the best arxiv query. "
            "When the tool returns, choose exactly the number of papers requested and pass "
            "them as concise JSON to the summarizer."
        ),
    )

    summarizer_agent = AssistantAgent(
        name="arxiv_summarizer_agent",
        description="An agent that summarizes arxiv papers.",
        model_client=openai_brain,
        system_message=(
            "You are an expert researcher. When you receive the JSON list of "
            "papers, write a literature review style report in Markdown:\n"
            "1. Start with a 2-3 sentence introduction to the topic.\n "
            "2. Then include one bullet per paper with: title (as Markdown link), "
            "authors, the specific problem tackled, and its key contribution.\n "
            "3. Close with a single-sentence takeaway"
        ),
    )

    return RoundRobinGroupChat(participants=[arxiv_researcher_agent, summarizer_agent], max_turns=2)

async def run_research(topic: str, num_papers: int, api_key: str):
    team = create_team(api_key)
    task = f"Conduct a literature review on the topic - {topic} and return exactly {num_papers} papers"

    result_text = ""
    async for msg in team.run_stream(task=task):
        if hasattr(msg, 'content'):
            result_text += str(msg.content) + "\n\n"

    return result_text

def run_asyncResearch(topic, num_papers, api_key):
    return asyncio.run(run_research(topic, num_papers, api_key))

if st.button("🔍 Generate Literature Review", type="primary"):
    if not topic:
        st.error("Please enter a research topic")
    elif not api_key:
        st.error("Please enter your OpenAI API key in the sidebar")
    else:
        with st.spinner("Researching... This may take a minute."):
            try:
                result = run_asyncResearch(topic, num_papers, api_key)
                st.session_state.result = result
                st.session_state.topic = topic
            except Exception as e:
                st.error(f"Error: {str(e)}")

if st.session_state.result:
    st.markdown("---")
    st.subheader(f"📖 Literature Review: {st.session_state.topic}")
    st.markdown(st.session_state.result)

    st.download_button(
        "💾 Download Report",
        st.session_state.result,
        file_name=f"literature_review_{st.session_state.topic.replace(' ', '_')}.md",
        mime="text/markdown"
    )

if st.button("🗑️ Clear Results"):
    st.session_state.messages = []
    st.session_state.result = None
    st.rerun()