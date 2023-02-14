# modo 1
# listaPokemon = open("pokemon_list.txt", "r")
# i = 0
# for palabra in listaPokemon:
#     i += 1
#     # print(palabra)
#
# print(i)


# modo 2
# listaPokemon = open("pokemon_list.txt", "r")
# oracion = listaPokemon.readline()
# i = 0
# while oracion != "" and i < 10:
#     print(oracion)
#     i += 1
#     oracion = listaPokemon.readline()
#
# print(i)

# modo 3
numero = int(input("Ingresar cantidad de pokemones: "))
listaPokemon = open("pokemon_list.txt", "r")
palabras = listaPokemon.readlines()
# print(palabras[0])


for i in range(numero):
    print(palabras[i])

# print(palabras)
