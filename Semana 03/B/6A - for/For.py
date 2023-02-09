cant_notas = int(input("Cantidad de notas: "))
suma = 0
for index in range(cant_notas):
    nota = float(input("Nota {}:".format(index + 1)))
    while nota < 0:
        nota = float(input("Nota {}:".format(index + 1)))

    suma += nota


print("Sumatoria:", suma)
print("El promedio es {}".format(suma/cant_notas))