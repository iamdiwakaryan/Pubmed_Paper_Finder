import streamlit as st
from dotenv import load_dotenv
import os

from phi.agent import Agent
from phi.model.huggingface import HuggingFaceChat
from phi.tools.pubmed import PubmedTools

# Load .env variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Streamlit UI setup
st.set_page_config(page_title="PubMed LLM Agent", layout="centered")
st.title("🧠 PubMed LLM Agent")
st.caption("Search biomedical literature using PubMed + Hugging Face LLaMA 3")

# Query input
query = st.text_input("🔍 Enter your query:", placeholder="e.g. advancements in cancer detection using AI")

# Run button
if st.button("Run Agent") and query:
    st.info("⚙️ Running agent with PubMed + LLM...")

    # Model and tools
    llm = HuggingFaceChat(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=1000,
        temperature=0.2,
        api_key=HF_TOKEN
    )

    pubmed_tool = PubmedTools(email=EMAIL, max_results=5)

    agent = Agent(
        name="PubMedAI",
        model=llm,
        tools=[pubmed_tool],
        show_tool_calls=True,
        markdown=True
    )

    with st.spinner("🧠 Thinking..."):
        try:
            # Get LLM + PubMed-enhanced response
            result = agent.run(query)
            st.subheader("📋 Summary (LLM + PubMed):")
            st.markdown(result.content)

            # Direct PubMed search results
            st.divider()
            st.subheader("📚 Raw PubMed Articles:")

            # Fetch article data directly from tool
            articles = pubmed_tool.search_pubmed(query=query, max_results=5)
            if not articles:
                st.warning("No PubMed articles found.")
            else:
                for i, article in enumerate(articles, 1):
                    title = article.get("title", "No title")
                    source = article.get("source", "Unknown source")
                    pub_date = article.get("pub_date", "Unknown date")
                    pmid = article.get("uid", None)

                    st.markdown(f"### {i}. {title}")
                    st.markdown(f"- 📅 Published: {pub_date}")
                    st.markdown(f"- 📰 Journal: *{source}*")

                    if pmid:
                        pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                        st.markdown(f"- 🔗 [View on PubMed]({pubmed_url})")

                        # Try a PMC download link (not guaranteed to exist)
                        pmc_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmid}/pdf/"
                        st.markdown(f"- 📄 [Try PDF (PMC)]({pmc_url})")

                    st.markdown("---")

        except Exception as e:
            st.error(f"❌ Error: {e}")
