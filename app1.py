import streamlit as st
from dotenv import load_dotenv
import os

from phi.agent import Agent
from phi.model.huggingface import HuggingFaceChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.pubmed import PubmedTools

# Load env variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
EMAIL = os.getenv("EMAIL", "you@example.com")

# ---------- UI Setup ----------
st.set_page_config(page_title="Smart LLM Agent", layout="centered", page_icon="🧠")

# Sidebar Info
with st.sidebar:
    st.title("🧠 Multi-Tool LLM Agent")
    st.markdown("This app uses a large language model (Meta LLaMA 3) and two tools:")
    st.markdown("- 🧬 **PubMed** for biomedical research")
    st.markdown("- 🌍 **DuckDuckGo** for general web search")
    st.markdown("It automatically picks the best tool based on your query.")
    st.markdown("**Example queries:**")
    st.code("What is ulcerative colitis?\nWhat's happening in France?\nNew AI methods for cancer detection")
    st.markdown("---")
    st.markdown("Made with ❤️ using [Phidata](https://github.com/phidatahq/phidata)")

st.markdown("<h1 style='text-align: center;'>🧠 Smart AI Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask medical or general questions — the AI will choose the right tool.</p>", unsafe_allow_html=True)

# ---------- User Input ----------
query = st.text_input("🔍 Enter your query below:", placeholder="e.g. What's happening in France?")

run_col, clear_col = st.columns([1, 1])
run_pressed = run_col.button("🚀 Run Agent")
clear_pressed = clear_col.button("🧹 Clear")

if clear_pressed:
    st.experimental_rerun()

# ---------- Agent Execution ----------
if run_pressed and query:
    st.info("🤖 Agent is reasoning with tools...")

    # Load model
    llm = HuggingFaceChat(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        api_key=HF_TOKEN,
        max_tokens=2048,
        temperature=0.3,
    )

    # Tool setup
    tools = [
        DuckDuckGo(),
        PubmedTools(email=EMAIL, max_results=5)
    ]

    # Agent init
    agent = Agent(
        name="SmartMultiAgent",
        model=llm,
        tools=tools,
        show_tool_calls=True,
        markdown=True
    )

    with st.spinner("💭 Thinking..."):
        try:
            response = agent.run(query)

            # Output
            st.success("✅ Agent has responded!")
            st.markdown("### 📋 Final Answer")
            st.markdown(response.content)

        except Exception as e:
            st.error(f"❌ Agent Error: {e}")
