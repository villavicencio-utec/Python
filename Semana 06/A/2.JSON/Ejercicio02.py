# Usando la información de la API https://reqres.in/api/users?page=1
# Se le pide implementar un programa que busque los datos completos del usuario “Emma” (first_name)
# Luego generalice la búsqueda para cualquier valor del campo.

import requests
import json

# parametro
name = "Emma"

url = "https://reqres.in/api/users?page=1"

result = requests.get(url).json()
result["data"]

def buscar_datosbasicos(nombre):
    for item in result["data"]:
        if nombre == item["first_name"]:
            print("email: ", item["email"])
            print("last_name: ", item["last_name"])
            print("avatar: ", item["avatar"])


buscar_datosbasicos("Eve")
# muestra el resultado
# print(json.dumps(result, indent = 4))
