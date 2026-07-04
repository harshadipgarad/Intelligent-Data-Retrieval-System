import streamlit as st
from pypdf import PdfReader
from langchain_ollama import OllamaLLM

st.title("📄 DocGPT")

model = OllamaLLM(model="llama3.2")

if "messages" not in st.session_state:
    st.session_state.messages = []

pdf = st.file_uploader("Upload PDF", type="pdf")

if pdf:
    reader = PdfReader(pdf)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    # Display old chats
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    question = st.chat_input("Ask a question")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        history = "\n".join(
            [f'{m["role"]}: {m["content"]}'
             for m in st.session_state.messages]
        )

        prompt = f"""
        Document:
        {text}

        Conversation History:
        {history}

        Question:
        {question}

        Answer:
        """

        answer = model.invoke(prompt)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()