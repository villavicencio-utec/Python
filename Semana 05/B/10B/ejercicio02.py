# Use un diccionario para crear un traductor de numeros del
# 1 al 10 al japonés. Tomar en cuenta la siguiente equivalencia.

dic = {
    1: "Ichi",
    2: "Ni",
    3: "San",
    4: "Yon",
    5: "Go",
    6: "Roku",
    7: "Nana",
    8: "Hachi",
    9: "kyu",
    10: "Ju"
}

numero = int(input("Input: "))

if numero>0 and numero <11:
    print("Output: ", dic[numero])
else:
    print("Numero fuera de rango")