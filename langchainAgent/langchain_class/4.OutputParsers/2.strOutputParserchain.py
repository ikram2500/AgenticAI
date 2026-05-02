from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class BlackHoleFacts(BaseModel):
    fact1: str = Field(description="first fact about black hole")
    fact2: str = Field(description="second fact about black hole")
    fact3: str = Field(description="third fact about black hole")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

structured_model = model.with_structured_output(BlackHoleFacts)

template = PromptTemplate(
    template="Give me 3 facts about {topic}",
    input_variables=["topic"]
)

chain = template | structured_model

result = chain.invoke({"topic": "Black hole"})

print(result)