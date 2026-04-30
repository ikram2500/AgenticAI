from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat template 
chat_template = ChatPromptTemplate([
    "system", "You are a very hlpful customer support agent",
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", '{query}')
])

# load chat history 
chat_history = []
with open("chatbot_history.txt") as file:
    chat_history.extend(file.readlines())

prompt = chat_template.invoke({
    "chat_history": chat_history,
    'query': 'where is my refund?'
})  

print(prompt)

