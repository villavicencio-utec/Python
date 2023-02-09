lista = ["Juan","Luis", "Almendra","Jorlan","Maria","Luisa"]

#Iteración por un elemento
for item in lista:
    print(item)
print()

#Iteración basada en el índice
for indice in range(len(lista)):
    if indice % 2 == 0:
        print(lista[indice])

print()

#enumerate cuando queremos usar el indice y elemento a la vez.
for indice, elemento in enumerate(lista):
    print("Indice [{}]: {}".format(indice, elemento))
