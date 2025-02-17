from langchain_ollama import OllamaLLM

# Tente uma frase mais simples
llm = OllamaLLM(model="llama3")
response = llm.invoke("Olá, mundo!")
print(response)
