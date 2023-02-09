import random as rd

FILA = 10
COLUMNA = 10
matriz = []
for i in range(FILA):
    fila = []
    for j in range(COLUMNA):
        valor = rd.randint(1, 10)
        fila.append(valor)

    matriz.append(fila)

print(matriz)

