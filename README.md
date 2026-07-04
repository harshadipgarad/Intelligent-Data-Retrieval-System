## Intelligent Data Retrieval System

An Intelligent Data Retrieval System that uses RAG and NL2SQL to answer questions from documents and databases. It retrieves relevant information and generates accurate, context-aware responses.

## 🏗️ Project Architecture & Workflow

The system operates entirely on local infrastructure, utilizing a two-phase Retrieval-Augmented Generation (RAG) architecture:

```text
========================================================================================
PHASE 1: INGESTION PIPELINE (vector_store.py)
========================================================================================
[Your PDF] ──> [Text Splitting] ──> [all-minilm Embeddings] ──> [Chroma DB (Local Store)]


========================================================================================
PHASE 2: RETRIEVAL & GENERATION PIPELINE (main.py)
========================================================================================
                                     ┌─────────────────────────┐
                                     │  Chroma DB Vector Store │
                                     └────────────┬────────────┘
                                                  │
                                            (Query Match)
                                                  │
                                                  ▼
[User Query] ───────────────────────────> [Retrieve Top 3 Chunks]
                                                  │
                                                  ▼
[User Query + Context + Chat History] ──> [Ollama (Llama3)] ──> [Streamlit UI Response]
========================================================================================


 🚀 Features

* **100% Local & Private:** No data leaves your machine. Processing is handled entirely offline.
* **Efficient Retrieval:** Uses `all-minilm` embeddings and Chroma DB for fast semantic search.
* **Context-Aware Chat:** Powered by `llama3` with session state management to remember conversation history.
* **User-Friendly UI:** Clean and interactive chat interface built with Streamlit.

---

💻 How to Run
Step 1: Initialize the Vector Store
Before launching the UI, generate your local vector database embeddings by running:

PowerShell
python vector.py
Note: Make sure your reference PDF is placed in the root directory and matches the pdf_path in vector.py.

Step 2: Start the Chat Application
Launch the Streamlit web interface:

PowerShell
streamlit run main.py