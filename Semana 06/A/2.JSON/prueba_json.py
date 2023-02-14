import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

# invoca el servicio web
# se recibe en un diccionario
result = requests.get(url)  # Genera la solicitud
formato_json = result.json()

# print(formato_json)

# muestra el resultado
print(json.dumps(formato_json, indent=4))
