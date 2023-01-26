# Promedio tres numeros
def promedio(a, b, c):
    """
    Promedio de tres numeros
    :param a:5
    :param b:3
    :param c:7
    :return:5.0
    """
    print("Funcion:",id(a),id(b),id(c))

    suma = a + b + c
    prom = suma / 3
    return prom


n1 = int(input("Ingrese n1 = "))
n2 = int(input("Ingrese n2 = "))
n3 = int(input("Ingrese n3 = "))

print("Main:",id(n1),id(n2),id(n3))

res = promedio(n1,n2,n3)

print(f"El promedio es {res}")