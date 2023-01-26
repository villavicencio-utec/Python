# Escribir un programa que permita hallar la suma de los valores
# enteros de los caracteres de una palabra, según su posición en el alfabeto.


def posicion(letra):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alfabeto.find(letra) + 1

def contar(palabra):
    suma = 0
    for letra in palabra.upper():
        suma += posicion(letra)

    return suma

palabra = input("Ingrese una palabra o letra: ")
print("Su valor es:", contar(palabra))



palabra = "Hola"
print(palabra.find("z"))

