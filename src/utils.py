import ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """"
    Responda a pergunta a seguir considerando o contexto apresentado.
    Contexto da conversa: {context}
    Pergunta: {question}
    Resposta:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def get_llama_response(usaer_message):
    result = chain.invoke({"context": "", "question": usaer_message})
    print(result)
    return result