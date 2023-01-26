# Condicional Simple

edad = int(input("Ingresar edad: "))  # 19

# if edad > 18:
#     print("Es mayor de edad")
#     print("VERDAD _ 1")
#     print("VERDAD _ 2")
#

# Condicional Doble
# if edad > 18:
#     print("Mayor de edad")
# else:
#     print("Menor de edad")


# Condicional multiple

# if edad > 18:
#     print("Mayor de edad")
# elif edad < 18 and edad > 0:
#     print("Menor de edad")
# else:
#     print("Negativo")


# Condicional anidada

if edad > 18:
    print("Mayor de edad")
elif edad < 18 and edad > 0:
    print("Menor de edad")
    if edad == 10:
        print("10 es el rango")
    else:
        print("10 no es el rango")
else:
    print("Negativo")
