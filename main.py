import streamlit as st
import tempfile
import os
import pandas as pd
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
st.set_page_config(page_title="Document Chatbot", page_icon="📄")
st.title("📄 DocGPT")
@st.cache_resource
def load_model():
    return OllamaLLM(model="llama3")
model = load_model()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "document_text" not in st.session_state:
    st.session_state.document_text = ""
with st.sidebar:
    st.header("Upload Section")
    uploaded_file = st.file_uploader(
        "Upload PDF, CSV or Excel",
        type=["pdf", "csv", "xlsx"]
    )
    if uploaded_file:
        file_name = uploaded_file.name
        extracted_text = ""
        if file_name.endswith(".pdf"):
            with st.spinner("Reading PDF structure..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                try:
                    loader = PyPDFLoader(tmp_path)
                    pages = loader.load()
                    extracted_text = "\n".join([page.page_content for page in pages])
                    st.success("PDF loaded perfectly!")
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
        elif file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            extracted_text = df.to_string()
            st.success("CSV loaded perfectly!")
        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
            extracted_text = df.to_string()
            st.success("Excel loaded perfectly!")
        st.session_state.document_text = extracted_text
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if question := st.chat_input("Ask a question about the document..."):
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("assistant"):
        if st.session_state.document_text:
            with st.spinner("Analyzing document details..."):
                template = """
                You are a highly precise Document Reader AI. Answer the question based ONLY on the document content provided below.
                Spell all student names, contact details, and skills exactly as written in the text.
                Do not make up facts or bring outside data.

                Document Content:
                {document}

                Question:
                {question}

                Answer:
                """
                prompt = ChatPromptTemplate.from_template(template)
                chain = prompt | model
                result = chain.invoke({
                    "document": st.session_state.document_text,
                    "question": question
                })
                st.markdown(result)
                st.session_state.messages.append({"role": "assistant", "content": result})
        else:
            st.warning("Please upload a document from the sidebar first!")