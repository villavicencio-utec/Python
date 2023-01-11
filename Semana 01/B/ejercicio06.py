from math import pi, tan

s = int(input("Longitud de los lados = "))
n = int(input("Número de lados = "))

area = (n*pow(s, 2))/(4*tan(pi/n))
print("Área =", area)