# Implemente un algoritmo que permita copiar un archivo a otro.
inputFile = open("numeros.txt","w")

for i  in range(0, 101):
    inputFile.write(str(i) + "\n")
# inputFileCopia = open("poema_2_copia.txt", "w+")
#
# for oracion in inputFile:
#     inputFileCopia.write(oracion)

