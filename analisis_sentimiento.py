import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analizar_sentimiento(texto, modelo="text-davinci-002"):
    prompt = f"Analizar el sentimiento predominante del siguiente texto: '{texto}'. El sentimiento es:\n"
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

texto_para_analizar = input("Ingresa el texto a analizar: ")
sentimiento = analizar_sentimiento(texto_para_analizar) 
print(sentimiento)