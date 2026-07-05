import streamlit as st
from pypdf import PdfReader
from langchain_ollama import OllamaLLM

st.title("📄 DocGPT")

model = OllamaLLM(model="llama3.2", temperature=0.1)

if "messages" not in st.session_state:
    st.session_state.messages = []

pdf = st.file_uploader("Upload PDF", type="pdf")

if pdf:
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    question = st.chat_input("Ask a question")

    if question:
        history = "\n".join(
            [f'{m["role"]}: {m["content"]}' for m in st.session_state.messages]
        )

        st.chat_message("user").write(question)
        st.session_state.messages.append({"role": "user", "content": question})

        prompt = f"""You are a helpful assistant. Answer the user's question accurately based ONLY on the provided Document context.
If the information is available in the document, extract it properly. Do not state that the information is missing if it is present below.

Document Content:
\"\"\"
{text}
\"\"\"

Previous Conversation History:
\"\"\"
{history}
\"\"\"

Current Question to Answer: {question}

Answer:"""

        with st.spinner("Thinking..."):
            answer = model.invoke(prompt)

        st.chat_message("assistant").write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})