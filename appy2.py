from langchain_ollama import OllamaLLM

# Inicializando o modelo
llm = OllamaLLM(model="llama3")

# Usando uma pergunta mais completa
response = llm.invoke("Como IA pode me ajudar nos negocios")

# Verificar tipo de resposta
if isinstance(response, dict):
    print("Resposta:", response.get('output', 'Sem saída'))
else:
    print("Resposta:", response)
