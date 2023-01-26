# Escribir un código en Python que reciba una frase e imprima el número de letras que la frase contiene.
# Por ejemplo: “hola”, tiene 4 letras.
# No use la función len.

frase = input("Ingrese frase: ")

cant = 0
for letra in frase:
    if letra != " ":
        cant += 1

print("Cantidad de letras es {}".format(cant))
