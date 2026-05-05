from langchain_core.tools import tool 

@tool 
def add(a:int, b:int) -> int:
    """Add two numbers"""
    return a + b 

@tool 
def mul(a:int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return (add, mul)
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tl in tools:
    print(tl.name, "--------", tl.description)

    