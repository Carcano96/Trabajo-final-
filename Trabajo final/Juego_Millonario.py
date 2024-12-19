import requests

def preguntas(numero=15):
    url = f"https://opentdb.com/api.php?amount={numero}&difficulty=easy&type=multiple"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']

















