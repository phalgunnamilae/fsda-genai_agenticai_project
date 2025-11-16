import streamlit as st
from langchain_community.document_loaders import UnstructuredFileIOLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnableParallel, RunnableLambda

# --------------------------------------------------------
# Streamlit UI
# --------------------------------------------------------
st.title("📘 RAG App using Ollama + LangChain + Chroma")
st.write("Upload a PDF and ask questions from it")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

# Process when file is uploaded
if uploaded_file is not None:

    if st.button("Build Vector DB"):
        with st.spinner("Reading PDF..."):
            loader = UnstructuredFileIOLoader(uploaded_file)
            data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
        docs = splitter.split_documents(data)

        with st.spinner("Generating embeddings & creating Chroma DB..."):
            embedder = OllamaEmbeddings(model="nomic-embed-text")

            vectordb = Chroma.from_documents(
                documents=docs,
                embedding=embedder,
                persist_directory="ollama_local_db"
            )

        st.success("Vector DB created successfully! You can now ask questions.")

    st.divider()
    st.subheader("Ask a question")

    question = st.text_input("Your question:")

    if question:
        with st.spinner("Retrieving & generating answer..."):

            vectordb = Chroma(
                persist_directory="ollama_local_db",
                embedding_function=OllamaEmbeddings(model="nomic-embed-text")
            )

            retriever = vectordb.as_retriever()
            llm = Ollama(model="mistral:latest")

            def format_prompt(inputs):
                return f"""
Use this context to answer:

Context:
{inputs['context']}

Question:
{inputs['question']}
"""

            rag_chain = (
                RunnableParallel({
                    "context": retriever,
                    "question": RunnableLambda(lambda x: x)
                })
                | RunnableLambda(format_prompt)
                | llm
            )

            response = rag_chain.invoke(question)

        st.write("### 🧠 Answer:")
        st.write(response)

else:
    st.info("Please upload a PDF to continue.")
