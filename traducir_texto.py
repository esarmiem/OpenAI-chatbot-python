import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def traducir_texto(texto, idioma, modelo="text-davinci-002"):
    prompt = f"Traducir el siguiente texto: '{texto}' al idioma {idioma}."
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

texto_para_traducir = input("Ingresa el texto a traducir: ")
mi_idioma = input("A que idioma lo quieres traducir: ")
traduccion = traducir_texto(texto_para_traducir, mi_idioma)
print(traduccion)