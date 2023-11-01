import openai
from os import environ as env
from dotenv import find_dotenv, load_dotenv
import json

# carga las variables de entorno
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# OpenAI
openai.api_key = env.get("OPENAI_API_KEY")

# Azure OpenAI
# openai.api_type = env.get("OPENAI_API_TYPE")
# openai.api_base = env.get("OPENAI_API_BASE")
# openai.api_version = env.get("OPENAI_API_VERSION")
# openai.api_key = env.get("OPENAI_API_KEY")


# Funcion para dividir un texto en pedazos
def split_text_with_overlap(text, chunk_size, overlap):
    chunks = []
    text_length = len(text)
    index = 0
    while index < text_length:
        end_index = index + chunk_size
        chunk = text[index:end_index]
        chunks.append(chunk)
        index = end_index - overlap
    return chunks


# Funcion para crear Tabla Markdown a partir de un texto
def gpt_tabla(tabla_incompleta, texto, doc_name):

    # openai.api_base = env.get("OPENAI_API_BASE_GPT-4")
    # openai.api_version = env.get("OPENAI_API_VERSION_GPT-4")
    # openai.api_key = env.get("OPENAI_API_KEY_GPT-4")

    prompt = """
    COMPLETA la TABLA INCOMPLETA con la información del TEXTO y retorna la TABLA COMPLETA.
    Si no encuentras la información, déjalo en blanco, no inventes ni agregues información.
    Puedes repetir el mismo patrón de campos si encuentras más personas o más propiedades.
    TABLA INCOMPLETA:
    """ + tabla_incompleta + """
    TEXTO:
    """ + texto + """
    TABLA COMPLETA:
    """

    mensajes = [
        {'role': 'user', 'content': prompt}
    ]
    tabla_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=mensajes,
        temperature=0.0
    )

    try:
        with open(f'./openai/azure/{doc_name}.json', 'w' ) as outfile:
            json.dump(tabla_gpt, outfile)
        with open(f'./openai/multiple-responses/{doc_name}.txt', 'w') as file:
            file.write(tabla_gpt['choices'][0]["message"]["content"])
    except Exception as e:
        print(e)
        pass

    return tabla_gpt['choices'][0]["message"]["content"]



# Funcion para unir multiples Tablas markdown en una sola con GPT
def gpt_union_tablas(listaDeTablas, doc_name):

    # openai.api_base = env.get("OPENAI_API_BASE_GPT-4")
    # openai.api_version = env.get("OPENAI_API_VERSION_GPT-4")
    # openai.api_key = env.get("OPENAI_API_KEY_GPT-4")

    prompt = """
    UNE las siguientes TABLAS en una sola TABLA.
    Solo si es necesario, puedes repetir el mismo patrón de campos dividiendo la información a fin tener una tabla más clara y ordenada.
    TABLAS A UNIR:
    """

    for tabla in listaDeTablas:
        prompt += tabla + "\n"

    mensajes = [
        {'role': 'user', 'content': prompt}
    ]
    tabla_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=mensajes,
        temperature=0.0
    )

    try:
        with open(f'./openai/azure/{doc_name}.json', 'w' ) as outfile:
            json.dump(tabla_gpt, outfile)
        with open(f'./openai/final-table/{doc_name}.txt', 'w') as file:
            file.write(tabla_gpt['choices'][0]["message"]["content"])
    except Exception as e:
        print(e)
        pass

    return tabla_gpt['choices'][0]["message"]["content"]
