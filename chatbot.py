import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load("es_core_news_md")
palabras_prohibidas = ["pregunta", "respuesta"]


def similitud_coseno(vector1, vector2):
    superposicion = np.dot(vector1, vector2)
    magnitud1 = np.linalg.norm(vector1)
    magnitud2 = np.linalg.norm(vector2)
    sim_cos = superposicion / (magnitud1 * magnitud2)
    return sim_cos

def es_relevante(respuesta, entrada, umbral=0.5):
    vector_respuesta = modelo_spacy(respuesta)
    vector_entrada = modelo_spacy(entrada)
    similitud = similitud_coseno(vector_respuesta, vector_entrada)
    return similitud >= umbral

def filtrar_listanegra(texto, listanegra):
    token = modelo_spacy(texto)
    resultado = []

    for t in token:
        if t.text.lower() not in listanegra:
            resultado.append(t.text)
        else:
            resultado.append("[PROHIBIDO]")

    return " ".join(resultado)


def preguntar_chat_gpt(prompt, modelo = "text-davinci-002"):
    response = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    respuesta_sin_listanegra = response.choices[0].text.strip()
    respuesta_filtrada = filtrar_listanegra(respuesta_sin_listanegra, palabras_prohibidas)
    return respuesta_filtrada

print("bienvenido al chatbot de OpenAI, escriba 'salir' para terminar")

while True: 
    conversacion_historica = ""
    ingreso_ususario = input("\nTu:")
    if ingreso_ususario.lower() == "salir":
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El Usuario pregunta: {pregunta}\nChatGPT responde: {respuesta}\n"

    prompt = f"El usuario pregunta: {ingreso_ususario}\n"
    conversacion_historica += prompt
    respuesta_chatgpt = preguntar_chat_gpt(conversacion_historica)

    relevante = es_relevante(respuesta_chatgpt, ingreso_ususario)

    if relevante:
        print(f"{respuesta_chatgpt}")
        preguntas_anteriores.append(ingreso_ususario)
        respuestas_anteriores.append(respuesta_chatgpt)
    else:
        print("La respuesta no es relevante.")



    

    preguntas_anteriores.append(ingreso_ususario)
    respuestas_anteriores.append(respuesta_chatgpt)