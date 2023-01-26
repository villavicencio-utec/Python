# Definicion o declaracion de funcion promedio

def promedio(a, b, c):
    suma = a + b + c #  suma = 8 + 6 + 14
    prom = suma / 3 #   prom = 28/3
    return prom

n1 = int(input("Ingrese n1 = "))
n2 = int(input("Ingrese n2 = "))
n3 = int(input("Ingrese n3 = "))
res = promedio(n1, n2, n3)

print(f"El promedio es {res}")

