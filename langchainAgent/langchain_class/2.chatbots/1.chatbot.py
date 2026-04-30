
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 

load_dotenv()
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower()=="exit":
        break 
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Bot:", result.content)

print("Chat history:", chat_history)