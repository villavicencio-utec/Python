import random

FILAS = 4
COLUMNAS = 4
M = []

def crearMatriz():
    for i in range(FILAS):
        M.append([0]*COLUMNAS)
        # [0 ,0 ,0 ,0, 0, 0]
        # [0 ,0 ,0 ,0, 0, 0]
        # [0 ,0 ,0 ,0, 0, 0]
        # [0 ,0 ,0 ,0, 0, 0]
        # [0 ,0 ,0 ,0, 0, 0]
        # [0 ,0 ,0 ,0, 0, 0]

def mostrarMatriz():
    print()
    for i in range(FILAS):
        for j in range(COLUMNAS):
            print(M[i][j], end=' ')
        print('')

def generarAleatorio():
    for i in range(FILAS):
        for j in range(COLUMNAS):
            M[i][j] = random.randint(-1, 9)

def sumarColumna(co):
    suma =0
    for i in range(FILAS):
        suma += M[i][co]
    return suma

def buscarNegativos():
    flag = False
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if M[i][j] < 0:
                flag = True
                break
    return flag


def cantNegativos():
    cant = 0
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if M[i][j] < 0:
                cant += 1
    return cant


def columnaCero(numero):
    cant = 0
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if M[i][j] == numero:
                cant += 1
                print("FILA {} - COLUMNA {} :".format(i, j))
    return cant

def sumatoriaDiagonal():
    suma = 0
    for i in range(FILAS):
        suma += M[i][i]


    for j in range(FILAS):
        suma += M[j][-j - 1]

    return suma

def maximoValor():
    mayor = 0
    indice_columna = -1
    indice_fila = -1

    for i in range(FILAS):
        for j in range(COLUMNAS):
            if M[i][j] > mayor:
                mayor = M[i][j]
                indice_columna = j
                indice_fila = i

    print("Elemento mayor", mayor)
    print("FILA {} - COLUMNA {} :".format(indice_fila, indice_columna))



print("Matriz de ceros")
crearMatriz()
mostrarMatriz()

print("Matriz con aleatorios")
generarAleatorio()
mostrarMatriz()
print("Cantidad de negativos:",cantNegativos())

print("Cantidad de ceros:",columnaCero(0))
print("Sumatoria diagonal:",sumatoriaDiagonal())
maximoValor()