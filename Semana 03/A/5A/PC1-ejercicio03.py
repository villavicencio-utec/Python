# Problema 03
# Autor: Jorge Villavicencio

numero = int(input("Numero [1 - 90] = "))
while numero < 1 or numero > 90:
    numero = int(input("Numero [1 - 90] = "))

i = 1
sumatoriaCubo = 0
while numero >= i:
    sumatoriaCubo += pow(i, 3)
    # sumatoriaCubo  =  sumatoriaCubo + pow(i, 3)
    i += 1

print("Sumatoria de cubos ({}) = {}".format(numero, sumatoriaCubo))


