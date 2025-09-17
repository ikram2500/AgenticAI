from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "what is the capital of France?")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.