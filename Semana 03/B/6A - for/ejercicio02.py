# Realice un programa que sume los números pares desde el 2 al 100.

suma = 0
for i in range(2,101):
    print(i)
    if i%2 == 0:
        suma= suma + i

print("Sumatoria 1 de número pares es {}".format(suma))

suma2 = 0
for i in range(0,101,2):
    print(i)
    suma2+=i

print("Sumatoria 2 de número pares es {}".format(suma2))

