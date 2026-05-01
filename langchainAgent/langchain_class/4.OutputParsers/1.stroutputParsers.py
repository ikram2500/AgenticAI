from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# ist prompt 
template1 = PromptTemplate(template="Write a detailed report on {topic})",
                            input_variables= ['topic'])

#prompt1 = template1.invoke({"topic":"English preimer league 2023/204"})

#result1 = model.invoke(prompt1).content
#print(result1)

# 2nd prompt
template2 = PromptTemplate(template="Write a 4 point summary on the followint {text}",
                            input_variables=['text'])



parser = StrOutputParser()

# chain 
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({ "topic":"English preimer league 2023/204"})
print(result)



#prompt2=template2.invoke({  'text': str(result1)})

#result = model.invoke(prompt2)
#print(result.content)

