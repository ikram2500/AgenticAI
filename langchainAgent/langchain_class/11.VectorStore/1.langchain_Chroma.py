from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_chroma import Chroma 
from langchain_core.documents import Document 
from dotenv import load_dotenv 

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



from langchain_core.documents import Document

doc1 = Document(
    page_content="Artificial Intelligence is transforming industries by automating tasks and improving decision-making.",
    metadata={"source": "ai_article_1", "topic": "AI"}
)

doc2 = Document(
    page_content="Machine Learning is a subset of AI that enables systems to learn from data without being explicitly programmed.",
    metadata={"source": "ml_article_1", "topic": "Machine Learning"}
)

doc3 = Document(
    page_content="Deep Learning uses neural networks with many layers to analyze complex patterns in data such as images and speech.",
    metadata={"source": "dl_article_1", "topic": "Deep Learning"}
)

doc4 = Document(
    page_content="Natural Language Processing allows computers to understand and generate human language.",
    metadata={"source": "nlp_article_1", "topic": "NLP"}
)

doc5 = Document(
    page_content="Computer Vision focuses on enabling machines to interpret and process visual information from the world.",
    metadata={"source": "cv_article_1", "topic": "Computer Vision"}
)

# combine the above docs
docs=[doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db",
    collection_name="sample"
)

vector_store.add_documents(docs)

vector_store.get(include=["embeddings","documents","metadatas"])

query = "which belong to machine learning"

result = vector_store.similarity_search(
    query=query,
    k=2
)

print(result)