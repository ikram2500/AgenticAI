from langchain_huggingface import HuggingFaceEmbeddings 
from dotenv import load_dotenv 
import os 
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of india"

documents=[
    "Delhi the capital of india"
    "kolkat the capital of east bengal"
    "Paris the capital of France"]


result = embeddings.embed_query(text)

#print(str(result))

result_doc = embeddings.embed_documents(documents)

similarity_score = cosine_similarity([result], result_doc)
print(similarity_score)
