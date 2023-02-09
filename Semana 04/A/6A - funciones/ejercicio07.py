def contarDigitos(numero):
    cant = 0
    while numero > 0:
        digito = numero % 10
        cant += 1
        numero = numero // 10

    return cant


n = int(input("Ingresar numero:"))
print("Cantidad de digits es", contarDigitos(n))
