## Intelligent Data Retrieval System

An Intelligent Data Retrieval System that uses RAG and NL2SQL to answer questions from documents and databases. It retrieves relevant information and generates accurate, context-aware responses.

## 🏗️ Project Architecture & Workflow

```text
                 PDF Document
                      │
                      ▼
             Text Chunking
                      │
                      ▼
      Generate Embeddings (all-MiniLM)
                      │
                      ▼
       Store in ChromaDB (Vector DB)
                      │
────────────────────────────────────────────
                User Query
                      │
                      ▼
      Retrieve Top Relevant Chunks
                      │
                      ▼
   Context + Query → Llama 3 (Ollama)
                      │
                      ▼
          Answer in Streamlit UI
```


✨ Features: PDF-Based Question Answering: Ask questions directly from uploaded PDFs. RAG Integration: Generates accurate responses using retrieved document context. Semantic Search: Retrieves relevant information using all-MiniLM embeddings and ChromaDB. 100% Local Processing: Ensures complete privacy by running entirely offline. Context-Aware Chat: Maintains conversation history for better responses. Interactive Streamlit UI: Provides a clean and user-friendly chat interface.


## 🚀 How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Initialize the Vector Store
```bash
python vector.py
```

### Run the Application
```bash
streamlit run main.py
```