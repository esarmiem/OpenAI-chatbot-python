import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Cual es la historia de la película Titanic?"

response = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

texto_generado = response.choices[0].text.strip()
print(texto_generado)

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)
print(analisis)

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

if ubicacion:
    prompt2 = f"La ubicacion de la película es {ubicacion.text}"
    response2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
