# Diseñe e implemente un algoritmo en Python que
# obtenga el promedio de un conjunto de números ingresados por el usuario.
# El usuario ingresará cero para indicar que ya no ingresará más números. El cero no se considera en el promedio.


x = int(input("Ingrese un numero ('0' para terminar): ")) # 20
suma = 0
cantNumero = 0
while x != 0:
    suma = suma + x #  suma =  35
    x = int(input("Ingrese un numero ('0' para terminar): ")) #  0
    cantNumero+=1 # cantNumero = 2


print("Promedio es = {}.".format(suma/cantNumero))



