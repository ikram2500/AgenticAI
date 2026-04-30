from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from typing import TypedDict 

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#schema 
class Review(TypedDict):
    summary: str 
    sentiment: str 

structured_model=model.with_structured_output(Review)

prompt = """
This hardware is great, but the software feels kind of bloated. So many boilerplate app. and my phone keepd hanging when i play PUBG.
"""

#result = structured_model.invoke(prompt)

#print(result)

new_prompt=f"generate sentiment and summary of the review given. The review is : '{prompt}'"
result = model.invoke(new_prompt)
print(result.content)