def sumarLetra(palabra):
    suma = 0
    for letra in palabra.upper():
        suma += ord(letra) - ord("A") + 1

    return suma

palabra = input("Ingrese una palabra o letra: ")
print("Su valor es:", sumarLetra(palabra))

print(ord("A"))
print(ord("B"))