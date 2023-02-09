# Dado una lista de valores, escriba un programa que permita identificar si un
# elemento se repite varias veces, luego proceder a dejar solo la primera ocurrencia del elemento
# y eliminar el resto de apariciones.

from random import randint

##inicializar la lista con numeros aleatorios
num = int(input("Numero de elementos: "))
lista = []  # declaro mi lista vacia

for cont in range(1, num + 1):
    valor = randint(1, 10)
    lista.append(valor)  # agregando elementos

print(lista)

# Solicitar numero repetido.
n = int(input("Numero repetido: "))
cant = 0
if n in lista:
    posicion = lista.index(n)
    aux = lista[posicion]
    lista[posicion] = "NO ELIMINAR"

    for item in lista:
        if item == n:
            lista.remove(n)

    print("Antes de actualizar",lista)
    lista[posicion] = aux
    print("Actualizado", lista)

else:
    print("Elemento no se encuentra en la lista")

# if n in lista:  # Valido existencia del elemento en la lista
#     for item in lista:
#         if item == n:
#             cant += 1
#
#     posicion = -1
#     if cant > 1:
#         posicion = lista.index(n)
#         lista[posicion] = "NO ELIMINAR"
#         print(lista)
#
#         for i in range(cant - 1):
#             lista.remove(n)
#
#         lista[posicion] = n
#
#     print(lista)
#
# else:
#     print("Elemento no se encuentra en la lista")
