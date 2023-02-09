# Elabore un algoritmo e implemente una función que permita hallar la hipotenusa de un triángulo rectángulo,
# dados los valores de sus catetos.
import math


def CalcularHipotenusa(a, b):
    c = math.sqrt(a**2 + b**2)  # raiz cuadrada
    return c


def areaTriangulo(a, b):
    area = (a*b)/2
    return area


numero1 = int(input("Ingrese el primer cateto:"))
numero2 = int(input("Ingrese el segundo cateto:"))
resp = CalcularHipotenusa(numero1, numero2)
area = areaTriangulo(numero1, numero2)
print(f"La hipotenusa es: {resp}")
print(f"Area es: {area}")
