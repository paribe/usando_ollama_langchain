# app.py
import streamlit as st
from langchain_ollama import OllamaLLM
import time

def initialize_llm():
    try:
        return OllamaLLM(model="llama3")
    except Exception as e:
        st.error(f"Erro ao inicializar o modelo: {e}")
        return None

def get_llm_response(llm, prompt):
    try:
        with st.spinner('Processando sua pergunta...'):
            response = llm.invoke(prompt)
            time.sleep(2)
            return response
    except Exception as e:
        st.error(f"Erro ao processar a resposta: {e}")
        return None

def main():
    st.title("🤖 Chat com Llama 3")
    st.write("Digite sua pergunta abaixo:")

    # Inicializa o modelo
    llm = initialize_llm()
    
    if llm:
        # Área de input do usuário
        user_input = st.text_input("Sua pergunta:", "")
        
        if st.button("Enviar"):
            if user_input:
                response = get_llm_response(llm, user_input)
                if response:
                    st.write("### Resposta:")
                    st.write(response)
            else:
                st.warning("Por favor, digite uma pergunta.")

if __name__ == "__main__":
    main()