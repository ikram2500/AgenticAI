from langchain_community.document_loaders import PyPDFLoader 

loader = PyPDFLoader("constitution.pdf")
docs = loader.load()

print(docs)