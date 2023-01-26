# Escribir un programa en Python que permita ingresar 3 edades e indique cuál es el mayor

edad1 = int(input("Ingresar edad 1: "))
edad2 = int(input("Ingresar edad 2: "))
edad3 = int(input("Ingresar edad 3: "))

if edad1 > edad2 and edad1 > edad3:
    mayor = edad1
elif edad2 > edad3:
    mayor = edad2
else:
    mayor = edad3

print("Numero mayor es", mayor)
