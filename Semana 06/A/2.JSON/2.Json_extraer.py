# 1. Importar JSON
import json

# 2. Modalidad de lectura
with open('universidad.json', "r") as json_file:  # r de read
    # 3. Leer la información en la variable data.
    data = json.load(json_file)


print(data[1]["name"])
# print(data)/
# print(data[0]["name"])
# print(data[0]["web_pages"])
# print('Edad: ' + str(data['edad']))
# print('Ciudad: ' + data['ciudad'])
# print()
