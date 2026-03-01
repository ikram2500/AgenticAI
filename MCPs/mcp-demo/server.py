from mcp.server.fastmcp import FastMCP
import ollama

# 1. Initialize the FastMCP server
mcp = FastMCP("Local Intelligence Server")

# 2. Define our tool using the decorator
@mcp.tool()
def analyze_data(raw_text: str, instruction: str) -> str:
    """
    Analyzes raw text using a local LLM based on specific instructions.
    Useful for summarizing logs, extracting entities, or formatting raw data.
    """
    
    # 3. Construct the prompt
    prompt = f"Follow this instruction: {instruction}\n\nData to analyze:\n{raw_text}"
    
    try:
        # 4. Call the local LLM via Ollama
        response = ollama.chat(
            model='deepseek-r1:1.5b', 
            messages=[
                {'role': 'system', 'content': 'You are a precise data analysis assistant.'},
                {'role': 'user', 'content': prompt}
            ]
        )
        
        # 5. Return the model's output
        return response['message']['content']
    
    except Exception as e:
        return f"Error processing data locally: {str(e)}"

# 6. Run the server
if __name__ == "__main__":
    mcp.run()