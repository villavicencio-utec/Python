import json

with open('sanvaletin.json') as json_file:
  # llena un diccionario con los datos leidos
  data = json.load(json_file)


# print(data)
print(json.dumps(data, indent=4))
