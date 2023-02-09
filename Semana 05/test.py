import random as rd

binarios = int(input("Cantidad de numeros binarios aleatorios: "))
while binarios < 2:
    binarios = int(input("Cantidad de numeros binarios aleatorios: "))

tam = int(input("Tamanio de binarios: "))
while tam < 2:
    tam = int(input("Tamanio de binarios: "))

for i in range(binarios):
    binario =rd.choices([0,1], k=tam)
    print("".join(map(str, binario)))
    #El método join() toma todos los elementos de un
    #iterable y los une en una cadena.
    #map() de Python es una función incorporada que permite procesar y
    #transformar todos los elementos de un iterable sin utilizar un
    #bucle for explícito, una técnica comúnmente conocida como mapeo.
