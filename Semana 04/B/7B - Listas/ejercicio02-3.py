#3
# Vecino más fuerte: encuentre el máximo para cada par de elementos continuos de una lista.
# 	input: [2, 4, 5, 2, 3, 8, 5, 1, 4]
# 	output: [4, 5, 5, 3, 8, 8, 5, 4]
lista = [2, 4, 5, 2, 3, 8, 5, 1, 4]
listaMaximos = []

for indice in range(len(lista)-1):

    if lista[indice] > lista[indice+1]:  # indice = 0   lista[0] > lista[1]
        listaMaximos.append(lista[indice])
    else:
        listaMaximos.append(lista[indice+1])

print(listaMaximos)