edad = int(input("Ingrese edad: "))

if edad >= 0 and edad <= 17:
    precio = 15
elif edad >= 18 and edad <=30:
    precio = 25
elif edad >= 31 and edad <=45:
    precio = 30
else:
    precio = 10


print("Costo de entrada es {}".format(precio))
