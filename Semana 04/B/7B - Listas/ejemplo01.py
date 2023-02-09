num = int(input("Numero de elementos :"))  # 7
lista = []

# Ingresando valores a la lista
for cont in range(1, num + 1):
    dato = int(input("Dato {}: ".format(cont)))
    lista.append(dato)

# ---- imprimimos la lista utilizando el while
print("Imprimimos los elementos de la lista utilizando while")
i = 0
while i < len(lista):  # i < 7
    print(lista[i], " ", end=" ")
    i = i + 1

print("\nImprimimos los elementos de la lista con el for ")
for elemento in lista:
    print(elemento, " ", end=" ")

print("\nImprimimos los elementos de la lista con el for con rango")
for i in range(len(lista)):
    print(lista[i], " ", end=" ")
