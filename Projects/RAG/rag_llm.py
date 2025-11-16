import requests
from langchain_community.document_loaders import UnstructuredFileIOLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnableParallel, RunnableLambda

url="https://www.umaryland.edu/media/umb/oaa/campus-life/ois/documents/Guide-to-U.S.-Healthcare-System.pdf"
response = requests.get(url)
with open('Guide-to-U.S.-Healthcare-System.pdf', 'wb') as f:
    f.write(response.content)

with open("Guide-to-U.S.-Healthcare-System.pdf", "rb") as f:
    loader = UnstructuredFileIOLoader(f)
    data = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = splitter.split_documents(data)

# Embeddings using Ollama CPU
embedder = OllamaEmbeddings(model="nomic-embed-text")

# convert the chunks to embedings and store in vector db
vectordb = Chroma.from_documents(documents= docs,
                                 embedding= embedder,
                                 persist_directory= "ollama_local_db")

#retriever

retriever = vectordb.as_retriever()

llm = Ollama(model="mistral:latest")   # runs on CPU if no GPU

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

response = rag_chain.invoke("What should we do in case of any medical emergencies?")
print(response)
