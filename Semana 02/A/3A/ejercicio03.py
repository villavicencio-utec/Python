# Escribir un programa en Python que permita ingresar un número del 1-12 y 
# muestre el mes que corresponde y la estación a la que pertenece. Ejemplo 1=Enero, Verano

# Verano: Enero - Marzo
# Otoño: Abril - Junio
# Invierno: Julio - Septiembre
# Primavera: Octubre - Diciembre

numero = int(input("Ingresar numero: "))

if numero == 1 or numero == 2 or numero == 3 : # if numero >= 1 and numero <= 3
    estacion = "Verano"
    if numero == 1:
        print("Enero")
    elif numero == 2:
        print("Febrero")
    else:
        print("Marzo")
elif numero == 4 or numero == 5 or numero == 6 : # if numero >= 4 and numero <= 6
    estacion = "Invierno"
    if  numero == 4:
        print("Abril")
    elif numero == 5:
        print("Mayo")
    else:
        print("Junio")
elif numero == 7 or numero == 8 or numero == 9 :
    estacion = "Primavera"
    if  numero == 7:
        print("Julio")
    elif numero == 8:
        print("Agosto")
    else:
        print("Septiembre")
elif numero == 10 or numero == 11 or numero == 12:
    estacion = "Otonio"
    if  numero == 10:
        print("Octubre")
    elif numero == 11:
        print("Noviembre")
    else:
        print("Diciembre")
else:
    estacion = "Fuera de rango"

print(estacion)

