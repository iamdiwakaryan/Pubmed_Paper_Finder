Here's a `README.md` for your Streamlit app using a smart multi-tool LLM agent:

---

# 🧠 Smart Multi-Tool LLM Agent

This is a Streamlit application that uses a **Meta LLaMA 3-based language model** with multiple tools to answer both **general** and **biomedical** queries. It automatically decides the best tool (PubMed or DuckDuckGo) to fetch relevant and accurate information based on your question.

---

## 🚀 Features

* **Meta LLaMA 3 (8B-Instruct)**: Powerful open-source language model from Meta, hosted via Hugging Face.
* **DuckDuckGo Search Tool** 🌍: For real-time, general web search.
* **PubMed Tool** 🧬: For accessing biomedical research papers using PubMed.
* **Smart Tool Selection**: The agent picks the appropriate tool depending on your question.
* **Easy-to-use UI**: Built with Streamlit for a clean, interactive experience.

---

## 🛠️ Built With

* [Streamlit](https://streamlit.io/)
* [Phidata](https://github.com/phidatahq/phidata)
* [Hugging Face Transformers](https://huggingface.co/)
* [PubMed API](https://pubmed.ncbi.nlm.nih.gov/)
* [DuckDuckGo Search API](https://duckduckgo.com/)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-llm-agent.git
cd smart-llm-agent

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
EMAIL=your_email@example.com
```

* `HUGGINGFACEHUB_API_TOKEN`: Required to access Meta LLaMA-3 via Hugging Face.
* `EMAIL`: Required for accessing PubMed (use your email to identify yourself to NCBI).

---

## 🚦 Run the App

```bash
streamlit run app.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 💡 Example Queries

* `What is ulcerative colitis?`
* `What's happening in France?`
* `New AI methods for cancer detection`

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ❤️ Acknowledgements

* Thanks to [Phidata](https://github.com/phidatahq/phidata) for the tool-based LLM framework.
* Model: [Meta-LLaMA-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
* Streamlit for making interactive AI apps simple to build.

---

Let me know if you want this published as a GitHub `README.md` with formatting tailored for GitHub display.
