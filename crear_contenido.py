import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Crear contenido para el tema {tema}\n\n"
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=temperatura,
    )
    return response.choices[0].text.strip()

def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Resumir el siguiente texto en español: {texto}\n\n"
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=temperatura,
    )
    return response.choices[0].text.strip()

tema = input("Elije un tema: ")
tokens = int(input("Elije el número de tokens: "))
temperatura = int(input("del 1 al 10, que tan creativo quieres que sea tu contenido: ")) /10
contenido_creado = crear_contenido(tema, tokens, temperatura)
print(contenido_creado)

original = input("Pega aqui el texto a resumir sin saltos de linea: ")
tokens = int(input("Elije el número de tokens: "))
temperatura = int(input("del 1 al 10, que tan creativo quieres que sea tu contenido: ")) /10
resumen = resumir_texto(original, tokens, temperatura)
print(resumen)

