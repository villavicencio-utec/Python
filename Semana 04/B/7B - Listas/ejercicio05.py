# Sin recorrer de inicio a fin reiterativamente una de las listas,
# encuentre la diferencia (elementos que están en la primera lista pero no en la segunda) entre dos listas.
# Dentro del resultado, no mostrar valores duplicados.

lista = [2, 5, 8, 19, 4, 3, 20, "hola", 15, 7, 18]
lista2 = [1, "hola", 0, 15]

lista3 = []
print("Lista 1:", lista)
print("Lista 2:", lista2)
for item in lista:
    if item not in lista2:
        lista3.append(item)

print("Lista resultado:", lista3)
