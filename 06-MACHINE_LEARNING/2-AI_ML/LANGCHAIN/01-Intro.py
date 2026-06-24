import requests
from langchain_ollama import ChatOllama


def llm_calling(input_data, model_to_use):
    llm = ChatOllama(model=model_to_use)
    return print(llm.invoke(input_data).content)


base_url = "http://localhost:11434/"
response_data = requests.get(base_url + "/api/tags")
available_models_list = {}
i = 0
for models in response_data.json()["models"]:
    available_models_list[i] = models["name"]
    i += 1
print(available_models_list)

print("Select the model to chat:\n")
for key, value in available_models_list.items():
    print(key, value)
choice = input("Enter the model number:")
if int(choice) in available_models_list:
    selected_model = available_models_list[int(choice)]
    llm_calling(input("Enter the Query:"), selected_model)
else:
    print("Invalid Model Selection")
