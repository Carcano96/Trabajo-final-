
""""""""""""""""
import requests

api_key = '14d90ee9bd7a05f8cfd8182f54f652cc'
ciudad = input("Introduce la ciudad: ")
lat=("")
lon=("")
limit=("")

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
respuesta = requests.get(url)

print(respuesta.status_code)
"""""""""""""""""""
print(respuesta.json())

"""""""""""""""""""
import requests
api_key = '14d90ee9bd7a05f8cfd8182f54f652cc'
url = f"https://jsonplaceholder.typicode.com/posts"

nuevo_post = { "title": "Mi primer post", "body": "Este es un ejemplo .", "userId": 1 }

respuesta = requests.post(url, json=nuevo_post)
print(respuesta.status_code)

print(respuesta.json())
"""""""""""""""""""""""

import requests

api_key = '14d90ee9bd7a05f8cfd8182f54f652cc'
correo = input("Introduce una dirección de correo electrónico: ")

url = f"https://leakcheck.net/api/v1?key={api_key}&check={correo}"
respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.json())








