import random as rd

cant = 10
lista_aleatorio = [rd.randint(2, 20) for _ in range(cant)]
print(lista_aleatorio)
cuadrados = [x**2 for x in lista_aleatorio]
print(cuadrados)
impares = [x for x in lista_aleatorio if x % 2 != 0 and x > 9]
print(impares)

