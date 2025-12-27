from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
load_dotenv()

class ResearchRespose(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
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

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools=[]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[],
    verbose=True
    
)

raw_response = agent_executor.invoke({ "query": "What is the impact of climate change on polar bears?"})