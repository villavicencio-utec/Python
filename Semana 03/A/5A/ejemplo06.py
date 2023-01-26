gorinkis = int(input("Numero de gorinkis: "))
while gorinkis <=3:
    gorinkis = int(input("Numero de gorinkis: "))

i=1
while i <=gorinkis:
    suma=0;
    j = 1
    while j <= 5:
        presion = int(input("Presion sistolica " + str(j) + ": "))
        suma += presion
        j += 1
    if suma/5 > 130:
        print("Ud. es hipertenso",end="")
    else:
        print("Ud. No es hipertenso", end="")
    print(", el promedio de su presion sistolica es " + str(suma/5) )
    i = i + 1
