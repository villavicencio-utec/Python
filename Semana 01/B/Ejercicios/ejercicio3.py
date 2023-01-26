# Escribir un programa que solicite al usuario su nombre y edad. Posteriormente, deberá indicarle en qué año cumplirá 100 años.

nombre = input("Ingresar nombres: ")
edad = int(input("Ingresar edad: "))
adicional = 100 - edad
anios_100 = 2023 + adicional
print("Estiamdo {}, en el año {} usted cumplira 100".format(nombre, anios_100))

