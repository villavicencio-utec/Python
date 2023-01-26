numero = int(input("Filas: "))  # 9
while numero < 1 or numero > 9:
    numero = int(input("Filas: "))

i = numero
while i > 0:  # i = 0
    j = 1
    while i >= j:  # 8 >= 1
        print(j, end="")  # 1234567
        j += 1
    print("")
    i -= 1

    # 123456789
    # 12345678
    # 1234567
    # 123456
    # 12345
    # 1234
    # 123
    # 12
    # 1


