# Escribir un programa que genere la lista de 20 números aleatorios
# entre 1 y 15.

from random import randint
lista3 = [randint(1, 15) for _ in range(20)]
print(lista3)