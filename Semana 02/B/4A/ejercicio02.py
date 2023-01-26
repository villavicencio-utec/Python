n = int(input("Valor de N: "))  # 10
suma = 0  # La variable que almacena el resultado
i = 1  # La cantidad de elementos
while n >= i:  # 10 >= 3  -> True
    suma = suma + pow(i, 5)  # 33 +33**5 = 33
    i += 1  # i = 3

print("La suma es: ", suma)
