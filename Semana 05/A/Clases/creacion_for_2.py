ALUMNOS = 3
NOTA = 5

matriz = []

for i in range(ALUMNOS):  # Cantidad de FILAS
    list_notas = []
    for j in range(NOTA):  # Cantidad de COLUMNAS
        nota = float(input("Ingresar evaluacion {} : ".format(j+1)))
        list_notas.append(nota)
    matriz.append(list_notas)



suma =  0
# Recorrido de matriz
for i in range(ALUMNOS):  # FILAS
    for j in range(NOTA):  # COLUMNAS
        print(matriz[i][j], end="\t")  # i = 1, j = 0
        suma = suma + matriz[i][j]
    print()

print("Sumatoria de notas", suma)
