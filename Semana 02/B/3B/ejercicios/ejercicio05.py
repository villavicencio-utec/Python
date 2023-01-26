import random

numero = random.randint(1, 10)
intento = 0
while intento != numero:
    intento = int(input("Intente adivinar el número: "))
    if intento == numero:
        print("Felicitaciones adivinó el número!!!")
    else:
        print("No adivinó. Siga intentando.")
        if numero > intento:
            print("El número a adivinar es mayor")
        else:
            print("El número a adivinar es menor")
