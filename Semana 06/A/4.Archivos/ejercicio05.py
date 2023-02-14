# Implemente un algoritmo que permita leer un archivo y escribirlo en otro pero al revés,
# es decir la última línea del archivo origen será la primera en el archivo destino.

documento = open("poema.txt","r")
documentoCopia = open("ejercicio05.txt","w+")
palabras = documento.readlines()

print(len(palabras))
for index  in range(0,len(palabras)):
    indice = -1*index
    documentoCopia.write(palabras[indice])