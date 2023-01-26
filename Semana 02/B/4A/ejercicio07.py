# Realice un programa, que permita leer un número entero mayor que uno y determine si el número es un número
# perfecto o no.
# Un número es Perfecto, cuando el número es igual a la suma de sus divisores positivos menores que él.
# El 6 es un número perfecto porque la suma de sus divisores:  1 + 2 + 3 es igual a 6.
# El 28 es un número Perfecto, porque la suma de sus divisores:  1 + 2 + 4 + 7 + 14 es igual a 28


# Parte 1: Validación
x = int(input("Ingrese numero mayor a 1: "))
while x <= 1:
    x = int(input("Ingrese numero mayor a 1: "))

# x = 5

i = 1
suma_divisores = 0
while x > i:  # 5 > 5 = False
    if x % i == 0:
        suma_divisores += i  # 1
    i += 1

if suma_divisores == x:
    print("Numero perfecto")
else:
    print("No es un numero perfecto")



