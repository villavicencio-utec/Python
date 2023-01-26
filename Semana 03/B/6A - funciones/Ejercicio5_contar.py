def contarDigitos(numero): # 1053
    cant = 0
    while(numero > 0):
        digito = numero % 10 #1 % 10 = 1
        cant += 1 # 4
        numero = numero // 10 #1 // 10 = 0

    return cant

n = int(input("Ingresar numero:"))
print("Cantidad de digitos es",contarDigitos(n))
