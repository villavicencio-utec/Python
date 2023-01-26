# Validacion
numero = int(input("Numero de filas: "))  # 8
while numero < 1 or numero > 9:
    numero = int(input("Numero de filas: "))

fila = 1
while numero >= fila:  # i = 1, 2, 3, 4, 5, 6, 7, 8
    columna = 1
    while fila >= columna:  # 3 >= 1
        print(columna, end="")  # 1
        columna += 1
    print("")
    fila += 1

# 1
# 12
# 123
#
