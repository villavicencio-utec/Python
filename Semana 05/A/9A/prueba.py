FILA = 6
COLUMNA = 6
matriz = []
x = 1
for i in range(FILA):
    auxiliar = []
    for j in range(COLUMNA):
        auxiliar.append(x)
        x = x + 1
    matriz.append(auxiliar) # [7, 8, 9, 10, 11, 12]

for i in range(FILA):
    for j in range(COLUMNA):
        print(matriz[i][j], end = "    ")
    print()


Total_fila = 0
Total_columna = 0

for item_1 in range(FILA):
    Total_columna = Total_columna + matriz[item_1][5]

for item_2 in range(COLUMNA):
    Total_fila = Total_fila + matriz[5][item_2]


print("Total FILA",Total_fila)
print("Total COLUMNA",Total_columna)