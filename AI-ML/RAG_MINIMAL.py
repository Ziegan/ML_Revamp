import os
from langchain_community.document_loaders import (
    DirectoryLoader, 
    TextLoader, 
    PyPDFLoader, 
    CSVLoader, 
    Docx2txtLoader, 
    UnstructuredExcelLoader
    )
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

class DocumentProcessor:
    """Handles loading and splitting multiple document types."""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        # Map extensions to their specific loaders
        self.loaders = {
            ".txt": TextLoader,
            ".pdf": PyPDFLoader,
            ".csv": CSVLoader,
            ".docx": Docx2txtLoader,
            ".xlsx": UnstructuredExcelLoader,
        }

    def load_and_split(self):
        print(f"--- Scanning directory: {self.folder_path} ---")
        all_docs = []
        
        # Iterate through defined loaders and pull files
        for ext, loader_cls in self.loaders.items():
            loader = DirectoryLoader(
                self.folder_path, 
                glob=f"**/*{ext}", 
                loader_cls=loader_cls,
                use_multithreading=True
            )
            loaded_docs = loader.load()
            if loaded_docs:
                print(f"Found {len(loaded_docs)} files with extension {ext}")
                all_docs.extend(loaded_docs)
        
        if not all_docs:
            print("No supported documents found!")
            return []

        # Split text into chunks
        # Chunk overlap is key so context isn't lost at the edges
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        chunks = text_splitter.split_documents(all_docs)
        print(f"--- Created {len(chunks)} text chunks ---")
        return chunks

class RAGSystem:
    """Handles VectorDB operations and LLM interaction."""
    def __init__(self, model_name="llama3.2:1b"):
        # Initializing the LLM and Embedding model
        self.model = ChatOllama(model=model_name)
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.vector_db = None

    def initialize_db(self, chunks):
        if not chunks:
            return False
        print("--- Initializing Vector Database... ---")
        # Creating a persistent database
        self.vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=self.embeddings,
            persist_directory="./db_storage"
        )
        print("--- VectorDB Ready ---")
        return True

    def ask(self, question):
        # Similarity search to retrieve relevant context
        relevant_docs = self.vector_db.similarity_search(question, k=4)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        template = """Answer the question based ONLY on the following context. 
        If the answer is not in the context, say you don't know.
        
        Context: {context}
        
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.model
        
        return chain.invoke({"context": context, "question": question})

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    path = input("Enter the folder path containing your documents: ").strip()
    
    if not os.path.exists(path):
        print("Error: Path does not exist.")
    else:
        # 1. Process
        processor = DocumentProcessor(path)
        data_chunks = processor.load_and_split()

        # 2. Setup (Only proceed if chunks were found)
        if data_chunks:
            rag = RAGSystem()
            if rag.initialize_db(data_chunks):
                # 3. Chat
                print("\nReady! Ask anything about your documents.")
                while True:
                    query = input("\nYour Question (or 'exit'): ")
                    if query.lower() == 'exit': break
                    
                    response = rag.ask(query)
                    print(f"\nAI:\n{response.content}")