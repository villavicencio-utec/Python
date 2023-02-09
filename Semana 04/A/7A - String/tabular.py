n = input("Escriba el nombre del curso : ")
num = int(input("Escriba cantidad de alumnos: "))

while (num<=1 and num >=10):
    num = int(input("Numero de alumnos [1-10]: "))

suma = 0
i = 1
while i <= num:
    x = int(input("Nota {}:".format(i)))
    suma = suma + x
    i =+ 1

prom = suma/num

print("Para el curso de", n, "el promedio de notas es", prom)
