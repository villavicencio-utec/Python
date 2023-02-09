d = {'nombre': 'Zara', 'edad': 7, 'clase': 'first'}
print("diccionario inicial: ", d)

del d['nombre']
print("diccionario luego de eliminar: ", d)

d.clear()  # Eliminar los elementos del diccionario
print("diccionario luego de eliminar: ", d)

del d  # Eliminar la variable
print("diccionario luego de eliminar: ", d)
