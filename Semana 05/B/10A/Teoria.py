lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = []
# for num in lista:
#     valor = num*10
#     x.append(valor)

x = [_ for _ in lista]
print(x)

pares = [num*10 for num in lista if num%2 == 0]
print(pares)





