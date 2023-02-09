numero = int(input("filas: "))
while numero < 0:
    numero = int(input("filas: "))

j = numero
for i in range(1, numero+1):
    linea = " "*j + "#"*i
    j -= 1
    print(linea)

# Hola*5
# HolaHolaHolaHola

