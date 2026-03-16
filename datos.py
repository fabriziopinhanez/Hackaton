# datos.py
import json

def cargar_preguntas():
    with open("Preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    return preguntas

