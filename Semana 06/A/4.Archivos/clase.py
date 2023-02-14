archivo = open("archivo_prueba.txt", "r")
# Recorrido 1 - utilizando FOR
# for palabra in archivo:
#     print(palabra)

# Recorrido 1 - utilizando readline()
# oracion = archivo.readline()
#
# while oracion != "":
#     print(oracion)
#     oracion = archivo.readline()

#modo 3
palabras = archivo.readlines()

for palabra in palabras:
    print(palabra)
#
# print(palabras)