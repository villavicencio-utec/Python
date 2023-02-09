# Por listas por comprensión, solicitar al usuario la cantidad de N de notas  y generar el promedio de notas resultante.
# Si la nota es mayor a 10.5 indicar que el alumno ha aprobado sino el mensaje "Siga intentando"

n = int(input("Cantidad de notas: "))
promedio = sum([float(input("Nota:")) for _ in range(n)])/n
print(promedio)
if promedio >= 10.5:
    print("Aprobado")
else:
    print("Siga intentando")
