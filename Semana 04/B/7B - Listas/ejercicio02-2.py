#2
# Sin recorrer explícitamente la lista de inicio a fin,
# encuentre todas las posiciones en las que se encuentra un elemento determinado en una lista.
lista = [8, 4, 3, 2, 1, 5, 6, 2, 1, 4, 5, 8, 9]
print(lista)
numero = int(input("Numero a buscar posiciones: "))
posicion = -2
if numero in lista:
    while posicion != -1:
        if numero in lista:
            posicion = lista.index(numero)
            lista[posicion] ="Encontrado"
            print(posicion, end=" ")
        else:
            posicion = -1

else:
    print("Numero no se encuentra en la lista.")

print()
print(lista)