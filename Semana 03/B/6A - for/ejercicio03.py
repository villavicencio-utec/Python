numero = int(input("filas: "))
while numero < 0:
    numero = int(input("filas: "))

# numero = 12
# j = 12


j = numero
for i in range(1, numero+1):
    linea = " "*j + "#"*i
    j -= 1
    print(linea)


