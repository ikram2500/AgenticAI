from langchain.agents import create_agent 
from langchain_ollama import ChatOllama 



llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0)

agent = create_agent(
    model=llm, 
    tools=[], 
    system_prompt="you are a helpful assistant that useses tools when needed",
    debug=False
    )
user_query = "What is the capital of France?"

result = agent.invoke({"messages": [{"role": "user", "content": user_query}]})

print(result["messages"][-1].content)