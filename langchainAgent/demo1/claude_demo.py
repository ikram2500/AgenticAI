from dotenv import load_dotenv 
from pydantic import BaseModel

from langchain_anthropic import ChatAnthropic 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search, wikipedia_search

load_dotenv() 

class ResearchRespose(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model_name="claude-opus-4-6")
parser = PydanticOutputParser(pydantic_object=ResearchRespose)


prompt = ChatPromptTemplate.from_messages (
    [
        ("system", """
         You are a helpful assistant that provides concise and accurate information.
         Answer the user query and use necessary tools.
         wrap the output in this format and provide no other text\n{format_instructions}
         """),
        
        ("placeholder", "{chat_history}"),
        ("human","{query}"), 
        ("placeholder","{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())



tools = [search, wikipedia_search]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant"
)

#agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("what can i help you")
raw_response = agent.invoke({
    "messages": [{"role": "user", "content": query}]
})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "Raw Response  -  ", raw_response)

