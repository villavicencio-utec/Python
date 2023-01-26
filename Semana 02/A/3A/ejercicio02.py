# Escribir un programa en Python que permita ingresar un número del 1-7 y 
# muestre su equivalente en letras. Ejemplo 1=Lunes, 2 Martes, etc., si esta fuera de rango mostrar el mensaje error

numero = int(input("Ingresar numero: "))

if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miercoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sabado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = "Fuera de rango"

print(dia)