from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate 
from langchain_community.vectorstores import FAISS 
from dotenv import load_dotenv 

load_dotenv() 

# Step 1: Indexing (Document ingestion)
video_id = "NQWfvhw7OcI"

try:
    yt_api = YouTubeTranscriptApi()
    transcript_list = yt_api.fetch(video_id=video_id, languages=['en'])
    #flaten the transcript to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
except TranscriptsDisabled:
    print("No captions available for the video")


# Step 2: Indexing(Text spliting)
splitter= RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks= splitter.create_documents([transcript]) 

print(len(chunks))

# step 3: Embedding generation and storing in vector database 
embedding_model= HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-l6-v2")
vector_store=FAISS.from_documents(chunks, embedding=embedding_model)

# step 4: Retriever 
retriever= vector_store.as_retriever(search_type="similarity", search_kwargs={"k":2})

prompt=PromptTemplate(
    template="You are a helpful assistant. Answer only from the provided transcript conten. If the context is insufficient. just answer I dont know \n context: {context} \n question: {question}",
    input_variables=["context", "question"]
)

question = "What is the langchain?"
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context": context_text, "question":question})

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
answer = model.invoke(final_prompt)

print(answer.content)