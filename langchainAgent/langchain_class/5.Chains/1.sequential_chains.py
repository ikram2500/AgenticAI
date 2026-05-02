from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(template="generate 3 detailed report on a {topic}",
                       input_variables=['topic'])

prompt2=PromptTemplate(template="generate a 3 point summary on following text {text}",
                       input_variables=['text'])

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

result =chain.invoke({'topic': "31 Atlas Interstellar Object"})

print(result)
