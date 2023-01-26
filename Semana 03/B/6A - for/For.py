suma = 0
cantidad = 0
for item in range(50,121,2):
    print(item)
    suma += item
    cantidad+=1

print("La sumatoria de numeros pares es:",suma)
print("La cantidad de elementos es:",cantidad)
print("El promedio es {}".format(suma/cantidad))