from itertools import chain

from click import prompt
from langchain_ollama import ChatOllama
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="qwen-stable:latest")

promptTemplate = PromptTemplate.from_template("Be Precise to the qury and to the answer ... dont tell anymore than needed .. strictly")
chain = promptTemplate | llm | StrOutputParser()
print(chain.invoke(input("Enter the Query For the LLM:")).content)
