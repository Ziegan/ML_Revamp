from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen-stable:latest")
print(llm.invoke(input("Enter the Query For the LLM:")).content)