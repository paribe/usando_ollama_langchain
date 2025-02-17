from langchain_ollama import OllamaLLM
import time

try:
    llm = OllamaLLM(model="llama3")
    print("Modelo carregado.")
    
    print("Invocando o modelo...")
    
    response = llm.invoke("O que é aprendizado profundo?")
    time.sleep(2)  # Aguarda um tempo para garantir que o modelo teve tempo de responder
    
    # Verifique a resposta
    if response:
        print("Resposta recebida:", response)
    else:
        print("Nenhuma resposta recebida.")
    
except Exception as e:
    print(f"Erro: {e}")




