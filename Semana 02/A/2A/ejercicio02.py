# import math
from math import sqrt

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

# distancia = sqrt( ((x2-x1)**2) + ( (y2-y1)**2 ) )
distancia = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))


print("Distancia entre puntos es: ", round(distancia,2))
