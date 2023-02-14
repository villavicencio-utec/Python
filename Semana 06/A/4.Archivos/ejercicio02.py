# poema = open("poema.txt","r")
#
# oracion = poema.readline()
# cant = 0
# while oracion != "":
#     for palabra in oracion.split(" "):
#         cant += 1
#     oracion = poema.readline()
#
#
# print("Cantidad de palabras es : ",cant)
# poema.close()


poema = open("poema.txt", "r")

oraciones = poema.readline()
cant = 0
while oraciones != "":
    lista = oraciones.split(" ")
    cant = cant + len(lista)
    oraciones = poema.readline()

print("Cantidad de palabras es : ", cant)
poema.close()
