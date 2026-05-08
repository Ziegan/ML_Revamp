import asyncio
from langchain_ollama import OllamaLLM
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool

# 1. Setup the Model (Stability first!)
llm = OllamaLLM(model="qwen-stable:latest", temperature=0.1)

# 2. Define your Tool
def magic_calculator(input_str):
    return "The answer is 42"

tools = [
    Tool(
        name="MagicCalculator",
        func=magic_calculator,
        description="Useful for when you need to answer life's mystery math."
    )
]

# 3. Define the ReAct Prompt Template (Strict format for 1B models)
template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

# 4. Create the Agent and Executor
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# 5. Run it
if __name__ == "__main__":
    response = agent_executor.invoke({"input": "What is the meaning of math according to the MagicCalculator?"})
    print(response["output"])
