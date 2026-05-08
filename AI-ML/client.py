import asyncio
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_agent():
    # Define the server parameters
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # 1. List tools from the MCP server
            mcp_tools = await session.list_tools()
            
            # 2. Format MCP tools for Ollama's API
            formatted_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema,
                    },
                }
                for tool in mcp_tools.tools
            ]

            # 3. Chat with Llama 3.2:1b
            response = ollama.chat(
                model='llama3.2:1b',
                messages=[{'role': 'user', 'content': 'What is the area of a circle with radius 5?'}],
                tools=formatted_tools,
            )

            # Check if the model wants to call a tool
            print(f"Model Response: {response['message'].get('content', 'Calling Tool...')}")
            
            if response['message'].get('tool_calls'):
                for call in response['message']['tool_calls']:
                    print(f"Executing tool: {call['function']['name']} with {call['function']['arguments']}")
                    # You would execute the tool via session.call_tool() here

if __name__ == "__main__":
    asyncio.run(run_agent())
