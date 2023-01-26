i = 0  # contar la cantidad de números
numero = int(input("Ingresar numero: "))  # 7
suma = numero
while numero != 0:  # 0 != 0  -> False
    numero = int(input("Ingresar numero: "))  # 0
    suma = suma + numero  # suma = 25 + 0 = 25
    i += 1  # i = 3

print(suma / i)  # promedio



