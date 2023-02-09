# Desarrolle un programa que permita leer el radio de un círculo y que muestre su área.
# Debe implementar la función CalcularAreaCirculo que recibirá como parámetros el radio y
# devolverá el área del círculo.

import math as mt
def CalcularAreaCirculo(radio):
    print(mt.pi)
    return mt.pi*pow(radio,2)

radio = int(input("Radio: "))
print("El área es:",CalcularAreaCirculo(radio))

