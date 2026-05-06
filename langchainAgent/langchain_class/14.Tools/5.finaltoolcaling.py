from langchain_core.tools import tool 
from langchain_core.messages import HumanMessage 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

@tool
def add (a: int, b:int) -> int:
    """Add two numbers"""
    return a + b

llm_with_tool = llm.bind_tools([add])


user_query = "Can you add 10 and 5?"
query = HumanMessage(user_query)

messages = [query]

result = llm_with_tool.invoke(messages)
messages.append(result)
print(result.tool_calls[0])

tool_result = add.invoke(result.tool_calls[0])
messages.append(tool_result)
final_result = llm_with_tool.invoke(messages)
print(final_result)
print(final_result.content)