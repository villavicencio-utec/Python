# Realice un programa que sume los números pares desde el 2 al 100.

# suma = 0
# iteracion = 0
# for i in range(2, 101):
#     iteracion += 1
#     if i % 2 == 0:
#         suma = suma + i
#
# print("Sumatoria 1 de número pares es {}".format(suma))
# print("Cantidad de iteraciones {}".format(iteracion))

suma2 = 0
iteracion = 0
for i in range(0, 101, 2):
    iteracion += 1
    # print(i)
    suma2 += i

print("Sumatoria 2 de número pares es {}".format(suma2))
print("Cantidad de iteraciones {}".format(iteracion))

