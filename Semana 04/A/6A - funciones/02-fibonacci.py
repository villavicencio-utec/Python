
# docString
def fibonacci(n):  # n = 4
    """ Esto es un codigo fibonacci
    Pruebas de Hola como estas"""
    # docstring -> la documentacion o los comentarios de que hace la funcion

    a, b = 0, 1
    for i in range(n):   # 0 , 1 , 2 , 3
        a = b
        b = a+b
        #iteracion i = 0:   a = 1, b = 1
        #iteracion i = 1:   a = 1, b = 2
        #iteracion i = 2:   a = 2, b = 3
        #iteracion i = 3:   a = 3, b = 5
    return a # 3

#F(1) = 1
#F(0) = 0

#F(2) = F(1) + F(0) = 1
#F(3) = F(2)+ F(1) = 2
#..
numero = int(input("Ingrese n = "))

termino = fibonacci(numero)
termino = fibonacci(numero)
termino = fibonacci(numero)
termino = fibonacci(numero)
termino = fibonacci(numero)


print(f"El termino es {termino}")