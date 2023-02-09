# ---------------------------------------------------------------------
# Dato de entrada: num (int)
# Dato de salida : lista con valores aleatorio, listaPares, listaImpares
# -----------------------------------------------------------------------
from random import randint

num = int(input("Numero de elmentos: "))
lista = []

for cont in range(1, num + 1):
    valor = randint(1, 100)
    lista.append(valor)
print(lista)

# ---- ahora formamos dos nuevas listas
listadePares = []
listadeImpares = []
#
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        listadePares.append(lista[i])
    else:
        listadeImpares.append(lista[i])

print()
print("Lista de pares: ")
print(listadePares)
print()
print("Lista de impares: ")
print(listadeImpares)
