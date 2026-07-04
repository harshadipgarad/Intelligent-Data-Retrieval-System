import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "your_document.pdf"
db_location = "./chrome_langchain_db"

embeddings = OllamaEmbeddings(model="all-minilm")

if not os.path.exists(db_location):
    loader = PyPDFLoader(pdf_path)
    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=db_location,
        collection_name="pdf_reviews"
    )
else:
    vector_store = Chroma(
        collection_name="pdf_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(search_kwargs={"k": 3})