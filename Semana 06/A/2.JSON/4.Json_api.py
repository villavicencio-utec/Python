import requests
import json

# parametro
pais = input("Ingrese nombre")
# url del API REST
url = "http://universities.hipolabs.com/search?country="+ pais

# invoca el servicio web
# se recibe en un diccionario
result = requests.get(url).json()


# muestra el resultado
print(json.dumps(result, indent = 4))


