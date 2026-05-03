from langchain_community.document_loaders import WebBaseLoader 
url = "https://www.kaggle.com/hmikraminfo" 

loader = WebBaseLoader(url)

docs = loader.load()

print(docs)