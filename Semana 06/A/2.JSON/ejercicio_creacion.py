# 1. Importar módulo de JSON
import json

# 2. Crear un diccionario puede ser dic simple o anidado
obj = {
    "nombre": "Jorge",
    "apellido": "Villavicencio",
    "distrito": "Los Olivos",
    "edad": 27
}

# 3. guardar en un archivo 2.JSON:
with open('jorge_informacion.json', 'w') as archivo:  # w - write , r - read
    # 4. escribir la información del diccionario en el archivo.
    json.dump(obj, archivo)
