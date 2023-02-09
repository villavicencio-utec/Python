#1
# Sin crear una lista adicional y sin usar slicing, invierta una lista.
lista = [1, 2, 3, 4, 5, "a", "C", "d"]
for i in range(len(lista)):
    aux = lista.pop()  # 5
    lista.insert(i, aux)
    #  iter 1: aux = 5 , lista = [5, 1, 2, 3, 4]
    #  iter 2: aux = 4 , lista = [5, 4, 1, 2, 3]
    #  iter 3: aux = 3 , lista = [5, 4, 3, 1, 2]
    #  iter 4: aux = 2 , lista = [5, 4, 3, 2, 1]

print(lista)





