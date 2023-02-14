# listaPokemon = open("poema_2.txt", "r")
# cant = 0
# oracion = listaPokemon.readline()
# while oracion != "":
#     cant += 1
#     oracion = listaPokemon.readline()
#
# print("Cantidad de lineas es ",cant)
# listaPokemon.close()


listaPokemon = open("poema_2.txt", "r")
cant = 0
oracion = listaPokemon.readlines()
print("Cantidad de lineas es ", len(oracion))
listaPokemon.close()


