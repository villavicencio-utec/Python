palabra_1 = input("Palaba 1: ")
palabra_2 = input("Palaba 2: ")

palabras_list_1 = [x for x in palabra_1]
# for x in palabra_1:
#     palabras_list_1.append(x)

palabras_list_2 = [x for x in palabra_2]

lista_comparador = []

for i in palabras_list_1:
    for j in palabras_list_2:
        if i == j:
            lista_comparador.append(i)


for i in lista_comparador:
    print(i , end = ",")



