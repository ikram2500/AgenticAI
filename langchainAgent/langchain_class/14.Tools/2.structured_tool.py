from langchain_core.tools import StructuredTool 
from pydantic import BaseModel, Field 

class MultiplyInpu(BaseModel):
    a:int= Field(description="The first number to multiply", required=True)
    b:int= Field(description="The second number to multiply", required=True)

def multiply_fun(a:int, b:int) -> int:
    return a*b 

multiply_tool=StructuredTool.from_function(
    func=multiply_fun,
    name="multiply",
    description="Multiplies two numbers",
    args_schema=MultiplyInpu
)
result=multiply_tool.invoke({"a":5, "b":4})
print(result)