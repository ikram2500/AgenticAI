from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel, Field  


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(gt=18 , lt=100, description="The person's age. must be greater than 18")
    city: str = Field(description="The city where the person live")

parser = PydanticOutputParser(pydantic_object=Person) 

template = PromptTemplate(template="""
give me the name, age and city of a fictional {place} person. make sure the age is  greater than 18 and less than 100. Return the response in following format:
{response_format}
""",
input_variables=['place'],
partial_variables={"response_format": parser.get_format_instructions})

chain = template | model | parser 

result =  chain.invoke({ 'place': 'Nepal' })

print(result)