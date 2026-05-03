from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_community.document_loaders import TextLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.vectorstores import FAISS 
from langchain_community.chains import RetrievalQA 

# Step #1 : load the credentials 
load_dotenv()

# Step 2: Load the document 
loader = TextLoader("docs.txt")
documents = loader.load()

# step 3: Split the text into similar chunks 
text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_spliter.split_documents(documents)

# step 4: Conver text embeddings and store in FAISS
embeddings= GoogleGenerativeAIEmbeddings(model="model/gemini-embedding-001")
vectostore = FAISS.from_documents(docs, embeddings)

# Step 5: Create a retrieever (fetches relevant documents)
retriever = vectostore.as_retriever()

# step 6: Initiate a model 
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Step 7: Create a retriever QA chain
chain = RetrievalQA.from_chain_type(llm=model, retriever=retriever)

# step 8: manually  quary the model and retrive relevant document
query = "What is key take aways from this document"
response = chain.invoke(query)

# Step 9: print answer
print(response)

