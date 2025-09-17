from agents import OpenAIChatCompletionsModel, Agent, Runner 
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

client = AsyncOpenAI(
    api_key="GOOGLE_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



agent = Agent(
    name="basic_agent", 
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-pro",openai_client=client)
)

query = "what is the capital of France?"
result = Runner.run_sync(
    agent, 
    query
)

print(result.final_output)