## Intelligent Data Retrieval System

An Intelligent Data Retrieval System that uses RAG and NL2SQL to answer questions from documents and databases. It retrieves relevant information and generates accurate, context-aware responses.

## 🏗️ Project Architecture & Workflow

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


✨ Features: PDF-Based Question Answering: Ask questions directly from uploaded PDFs. RAG Integration: Generates accurate responses using retrieved document context. Semantic Search: Retrieves relevant information using all-MiniLM embeddings and ChromaDB. 100% Local Processing: Ensures complete privacy by running entirely offline. Context-Aware Chat: Maintains conversation history for better responses. Interactive Streamlit UI: Provides a clean and user-friendly chat interface.

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