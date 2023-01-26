# Escriba un programa que reciba un número
# representando una cantidad de segundos. Posteriormente, el programa deberá calcular cuántos minutos y segundos hay en ese tiempo. Por ejemplo: 150 segundos -> 2 minutos 30 segundos.

segundos = int(input("Ingresar segundos: ")) # 70
minutos = segundos // 60  # 1
residuo = segundos % 60 # 10

print("{} minutos {} segundos.".format(minutos, residuo))
