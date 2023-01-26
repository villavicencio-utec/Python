nNotas = int(input("Ingresar notas"))
suma = 0
cn = 1
while cn <= nNotas:
    nota = float(input("Nota %d : " % (cn)))

    while nota < 0 or nota > 20:  # F or F -> F
        nota = float(input("Nota %d : " % (cn)))

    suma += nota
    cn = cn + 1
print("Promedio",suma/nNotas)
