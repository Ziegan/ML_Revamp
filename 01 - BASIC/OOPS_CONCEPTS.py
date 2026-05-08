##ENCAPSULATION
print("#### ENCAPSULATION ####")
class LLMCONFIG:
    def __init__(self, api_key):
        self.__api_key = api_key
    
    def get_masked_key(self):
        return self.__api_key
    
config = LLMCONFIG("1234567890abcdefgh")
print(config.get_masked_key())


##ABSTRACTION
print("\n\n#### ABSTRACTION ####")
from abc import ABC, abstractmethod

class VectorStore(ABC):
    @abstractmethod
    def search(self, query):
        pass

class PineconeStore(VectorStore):
    def search(query):
        return f"Searching Pinecone for: {query}"

store = PineconeStore
print(store.search("data to search"))

##INHERITANCE
print("\n\n#### INHERITANCE ####")
class BaseModel:
    def __init__(self, version):
        self.version = version
    def info(self):
        print("Model Version: ", self.version)

class ChatModel(BaseModel):
    def chat(self, msg):
        return f"Chatting: {msg}"

my_chat = ChatModel("v2.0")
my_chat.info()

##POLYMORPHISM
print("\n\n#### POLYMORPHISM ####")
class OpenAI:
    def call(self): return "Response from OpenAI"

class Anthropic:
    def call(self): return "Response from Anthropic"

for model in [OpenAI(), Anthropic()]:
    print(model.call())