from llama_index.llms.ollama import Ollama
llm = Ollama(model="llama3.2")

response = llm.complete(input("Enter your query : "))
print(response)


