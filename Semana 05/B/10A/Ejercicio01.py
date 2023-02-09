# Escribir un programa que genere la lista de números entre 0 y 50
# que no sean pares y que no sean múltiplos de 3.

lista1 = [x for x in range(0, 51) if (x % 2 != 0 and x % 3 != 0)]
print(lista1)
