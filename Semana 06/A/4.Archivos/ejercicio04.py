# Implemente un algoritmo recibir texto desde el teclado hasta que se ingrese la palabra “fin”.
# Cada texto ingresado deberá ser guardado en un archivo.

inputFileCopia = open("ejercicio04.txt","w+")
entrada = input("Texto: ")
while entrada != "fin":
    inputFileCopia.write(entrada+"\n")
    entrada = input("Texto: ")


