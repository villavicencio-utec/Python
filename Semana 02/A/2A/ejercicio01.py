pesoGr = float(input("Ingrese el peso en grs: "))
alturaCm = float(input("Ingrese la altura en cms: "))

pesoKg = pesoGr/1000
alturaMtr = alturaCm/100

bmi = pesoKg/(alturaMtr*alturaMtr)
print("El índice de masa corporal (BMI) es igual a:", bmi)
print("El índice de masa corporal (BMI) es igual a: with round ", round(bmi, 3))
