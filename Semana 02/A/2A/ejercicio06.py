from math import pi, tan

s = float(input("Longitud de los lados = "))
n = int(input("Número de lados = "))

x = s**2
area = (n*pow(s, 2))/(4*tan(pi/n))
print("Área =", area)

# Generar el area con precision decimal 3
print("Área =", round(area, 3))

