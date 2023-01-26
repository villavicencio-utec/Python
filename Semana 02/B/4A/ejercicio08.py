# Una veterinaria le ha solicitado crear un programa para calcular
# la edad aproximada humana de sus pacientes caninos. El programa que usted realizará solicita un número N
# que indica cuántos pacientes se atenderán. A continuación solicita la edad canina y el nombre de cada paciente.
# Por cada lectura, usted imprime el nombre y la edad real aproximada humana:
#
# Considere que la edad real aproximada se calcula con los siguientes criterios.

cantidad = int(input("Numero de perritos: "))

i = 0
while cantidad > i:
    nombre = input("Nombre de perrito: ")

    edad = int(input("Edad canina: "))
    while edad < 1:
        edad = int(input("Edad canina: "))

    if edad <= 2:
        resultado = 10.5
    else:
        resultado = 10.5 + 4 * (edad-2)

    print("La edad de", nombre, "es de", resultado)
    i += 1

