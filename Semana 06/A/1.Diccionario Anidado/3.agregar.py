people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)
# crear un diccionario vacio "3" en el diccionario "people"
people[3] = {}
print(people)
# agregar los pares key:value al diccionario "3"
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people)

#1.json. agreguen un elemento 5 con un diccionario con 3 campos de valor.
people[5] = {}

# agregar los pares key:value al diccionario "3"
people[5]['name'] = 'Luna'
people[5]['age'] = '24'
people[5]['sex'] = 'Female'
#2. agreguen un elemento 4 con el string "PRUEBA  CLASE" de valor.
people[4] = "PRUEBA  CLASE"


print(people)



people2 = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

# agregar nuevo diccionario
people2[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}

print(people2)



