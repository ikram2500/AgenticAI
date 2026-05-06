from langchain_core.tools import tool 
from langchain_core.messages import ToolMessage, HumanMessage 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.tools import InjectedToolArg 
from typing import Annotated 

load_dotenv()

@tool 
def get_conversion_rate(base_currency: str, target_currency: str) -> float:
    """Return the real time currency conversion rate from base currency to target currency using time API"""
    conversion_rate=140.3
    return conversion_rate

@tool 
def convert(base_currency_value: float, conversion_rate:Annotated[float,InjectedToolArg]) -> float:
    """Converts a base value target currency value using conversion rate"""
    return base_currency_value*conversion_rate 

llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")
llm_with_tools= llm.bind_tools([get_conversion_rate, convert])

query = "What is the conversion factor between USD and NPR and based on it. Can you convert 10 USD to NPR?"

message = [HumanMessage(content=query)]
ai_msg = llm_with_tools.invoke(message)
message.append(ai_msg)

while ai_msg.content== "" and ai_msg.tool_calls:
    tool_message=[]

    for tool_call in ai_msg.tool_calls:
        tool_name=tool_call["name"]
        tool_id=tool_call["id"]
        tool_args=tool_call["args"]

        print(f"Execute too : {tool_name} with args: {tool_args}")

        if tool_name== "get_conversion_rate":
            rate=get_conversion_rate.invoke(tool_args)
            tool_output = str(rate)
            conversion_rate = rate 
        elif tool_name=="convert":
            if "conversion_rate" not in tool_args:
                if "conversion_rate" not in locals() or conversion_rate is None:
                    raise ValueError("Conversion rate is required but is not found")
                    tool_args["conversion_rate"]==conversion_rate
            converted_value==convert.invoke(tool_args)
            tool_output=str(converted_value)
        else:
            tool_output="Unknown tool : (tool_name)"
        tool_msg=ToolMessage(content=tool_output, tool_call_id=tool_id)
        tool_message.append(tool_msg)
    message.extend(tool_message)
    ai_msg=llm_with_tools.invoke(message)
    message.append(ai_msg)

result = message[-1]
print(result.content)

