from langchain_core.tools import tool 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@tool 
def add(a:int, b:int) -> int:
    """Adds two numbers"""
    return a+b 

llm_with_tools= model.bind_tools([add])
result= llm_with_tools.invoke("Can you add 3 with 14?")
print(result)