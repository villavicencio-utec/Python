import random

numero = random.randint(1, 10)  # numero =  2

intento = 0
while intento != numero: #  2 != 2 -> False
   intento = int(input("Intente adivinar el número: "))     # 2
   if intento == numero:  # 2 == 2 -> True
       print("Felicitaciones adivinó el número!!!")
   else:
       print("No adivinó. Siga intentando.")

