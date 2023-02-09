matriz = []

FILAS = 6
COLUMNAS = 7

for i in range(FILAS): #
    filas = ["1"]*COLUMNAS
    matriz.append(filas)

#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1

lista = [1,2,3]
lista[2] = 5
print(matriz[1][6])

matriz[1][6] = 100


