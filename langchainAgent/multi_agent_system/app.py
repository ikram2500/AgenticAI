import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="Research Pipeline", page_icon="🔍", layout="wide")

st.title("🔍 Multi-Agent Research Pipeline")

st.markdown("Enter a topic to run the research pipeline with Search → Reader → Writer → Critic agents.")

topic = st.text_input("Enter research topic:", placeholder="e.g., Quantum computing advances 2026")

if st.button("Run Research", type="primary"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Running research pipeline..."):
            try:
                state = run_research_pipeline(topic)
                
                st.success("Research completed!")
                
                st.header("📋 Step 1: Search Results")
                st.text_area("Search Results", state["search_result"], height=200)
                
                st.header("📄 Step 2: Scraped Content")
                st.text_area("Scraped Content", state["scraped_content"], height=300)
                
                st.header("📝 Step 3: Final Report")
                st.text_area("Final Report", state["report"], height=400)
                
                st.header("💡 Step 4: Critic Feedback")
                st.text_area("Critic Feedback", state["feedback"], height=200)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")