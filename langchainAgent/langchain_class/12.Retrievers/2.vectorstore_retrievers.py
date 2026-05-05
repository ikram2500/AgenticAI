from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_core.documents import Document 
from dotenv import load_dotenv 

load_dotenv()

from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain is a framework for building applications powered by large language models."),
    Document(page_content="It enables chaining of components like prompts, models, and retrievers into workflows."),
    Document(page_content="LangChain supports integrations with vector databases for retrieval-augmented generation."),
    Document(page_content="It provides tools for memory, agents, and document processing in AI applications.")
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="simple"
)

retriever = vector_store.as_retriever(search_kwards={'k':2})

query ="What does embedding do?"

result = retriever.invoke(query)

print (result)