import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def clasificar_texto(texto, modelo="text-davinci-002"):
    categorias = [
        "arte",
        "ciencia",
        "deporte",
        "economia",
        "educacion",
        "entretenimiento",
        "politica",
        "religion",
        "salud",
        "tecnologia",
    ]

    prompt = f"Clasificar el siguiente texto: '{texto}' en una de estas categorias: {', '.join(categorias)}. La categoria es: "
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


texto_a_clasificar = input("Ingresa el texto a clasificar: ")
categoria = clasificar_texto(texto_a_clasificar)
print(f"La categoria del texto es: {categoria}")