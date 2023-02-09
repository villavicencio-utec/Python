# docString
import math as mt
def fibonacci(n):
    """Calcula el termino n de la serie de Fibonacci
    Esta funcion calcula el termino n-esimo de la Serie de Fibonacci.
    Recibe como parametro un numero entero que representa el termino n
    que se requiere que calcule, empezando por el termino 0.
    :param n: 12
    :return: 144
    """
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

numero = int(input("Ingrese n = "))

termino = fibonacci(numero)

print(f"El termino es {termino}")


x = mt.sqrt(25)