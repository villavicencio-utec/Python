import random as rd

matriz = []

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

for i in range(filas):
    lista_row = []
    for j in range(columnas):
        lista_row.append(rd.randint(1,100))
    matriz.append(lista_row)


for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end ="\t")
    print()


FILA = 0
suma = 0
for i in range(columnas):
    suma += matriz[FILA][i]

FILA = filas-1
for i in range(columnas):
    suma += matriz[FILA][i]

COLUMNA = 0
for j in range(1,filas-1):
    suma += matriz[j][COLUMNA]

COLUMNA = columnas-1
for j in range(1,filas-1):
    suma += matriz[j][COLUMNA]


print(suma)





