# Sin recorrer de inicio a fin reiterativamente una de las listas,
# encuentre los elementos en común entre dos listas. Dentro del resultado, no mostrar valores duplicados.
# Encuentre los elementos comunes de dos listas.
# Crear una nueva lista en donde deben estar solamente los elementos comunes sin valores duplicados.

lista = [2, 5, 8, 19, 4, 3, 20, "hola", 15, 20, 18]
lista2 = [1, "Hola", 0, 15]

lista3 = []
print(lista)
print(lista2)
for i in lista2:
    if i in lista:
        lista3.append(i)

print(lista3)
