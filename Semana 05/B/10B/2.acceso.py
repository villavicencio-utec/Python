d = {'nombre': 'Zara', 'edad': 7}
print("d['nombre']: ", d['nombre'])
print("d['edad']: ", d['edad'])
# Acceso a clase no existente - Genera KeyError
# print(d["luis"])

d5 = {1: "Lunes",
      2: "Martes",
      3: "Miercoles",
      4: "Jueves",
      5: "Viernes",
      6: "Sabado",
      7: "Domingo"}

for item in d5:
    if item % 2 == 0:
        print(d5[item])

# print(d5.keys())
# print(d5.values())
