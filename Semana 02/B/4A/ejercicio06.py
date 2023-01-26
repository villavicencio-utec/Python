# Realice un programa, que permita leer varios números enteros hasta que se introduzca el cero.
# Luego el programa mostrará lo siguiente:
# La cantidad de números leídos
# La cantidad de números pares
# La cantidad de números impares
#
# El cero, no debe entrar en el conteo.
x = int(input("Numero  ('0' para terminar): "))  # 5

leidos = 0
pares = 0
impares = 0

while x != 0:  # 0 != 0 -> False
    if x % 2 == 0:
        pares += 1  # pares = pares + 1
    else:
        impares += 1  # impares = impares + 1

    leidos += 1  # leidos = leidos + 1
    x = int(input("Numero  ('0' para terminar): "))  # 0


print("Numeros leidos: ", leidos)
print("Numeros pares: ", pares)
print("Numeros impares: ", impares)

