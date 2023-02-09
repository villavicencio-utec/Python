def promedio_alumno(matriz, filas, columnas):
    sumatoria_total = 0
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma = suma + matriz[i][j]
            sumatoria_total = sumatoria_total + matriz[i][j]
        print("Promedio = {}".format(suma/columnas))
    print("Sumatoria Total {}".format(sumatoria_total))


def mostrar_matriz(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print("%20s"%matriz[i][j], end ="  ")  # "%10s"
        print()

alumnos = int(input("Cantidad de alumnos: ")) #FILAS
notas = int(input("Cantidad de notas: ")) #Columnas

matriz_notas = []
for i in range(alumnos):
    nombre = input("ALUMNO {}: ".format(i+1))
    nota_list = []
    for j in range(notas):
        nota = float(input("Nota {} = ".format(j+1)))
        nota_list.append(nota)
    matriz_notas.append(nota_list)



print("------------MOSTRAR MATRIZ---------------")
mostrar_matriz(matriz_notas, alumnos, notas)

promedio_alumno(matriz_notas, alumnos, notas)
