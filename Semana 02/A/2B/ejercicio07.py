numero1 = int(input("Numero 1 : "))
numero2 = int(input("Numero 2 : "))
numero3 = int(input("Numero 3 : "))

minimo = min(numero1,numero2,numero3)
maximo = max(numero1,numero2,numero3)

if ( numero1 !=minimo and numero1 !=maximo ):
    medio = numero1
elif( numero2 !=minimo and numero2 !=maximo ):
    medio = numero2
else:
    medio = numero3

print(minimo,medio,maximo)