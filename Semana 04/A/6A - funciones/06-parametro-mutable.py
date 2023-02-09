
def funcion(a, b):
    for i in range(len(a)):
        a[i] = a[i]*2
    for i in range(len(b)):
        b[i] = b[i]*3


x = [1, 2]
y = [3, 4, 5]
print("antes de la función", x, y)
funcion(x, y)  # parametros por referencia example. Lista
print("despues de la función", x, y)

