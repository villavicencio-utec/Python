# Desarrolle un programa que permita hallar el factorial de un número entero positivo mayor que cero.
# El programa debe validar el ingreso del dato, de tal manera que solo acepte números mayores o iguales a 1.


# Parte 1 - Validación

# Forma 1
flag = False
while not flag:  # not True  -> False
    n = int(input("Numero [mayor o igual a 1]: "))  # 0
    if n >= 0 and n <= 20:  # True and   -> True
        flag = True

# Forma 2
# n = int(input("Número: "))  # 5
# while n < 1:
#     n = int(input("Numero: "))  # -1


# Parte 2 - Factorial
i = 2
fact = 1
while n >= i:  # 5 >= 6  ->  False
    fact = fact * i  # 1*2
    i += 1

# iter 1,  fact = 2  ,  i = 3
# iter 2,  fact = 2*3  ,  i = 4
# iter 3,  fact = 2*3*4 ,  i = 5
# iter 4,  fact = 2*3*4*5 ,  i = 6   -> fact =  120 , i  = 6

print("El factorial es", fact)


