# Haciendo uso de un diccionario, implemente un algoritmo que permita determinar cuántas veces se repite
# cada carácter de un string. Considere que su algoritmo debe considerar cualquier caracter
# (letras, números, símbolos, etc.) excepto espacios en blanco.

# palabra = input("Input: ") #
# dic = {}
# for letra in palabra:
#     if letra != " ":
#         if letra in dic:
#             dic[letra] = dic[letra]+1
#         else:
#             dic[letra] = 1
#
# print(dic)



# Haciendo uso de un diccionario, implemente un algoritmo que permita determinar cuántas veces se repite
# cada carácter de un string. Considere que su algoritmo debe considerar cualquier caracter
# (letras, números, símbolos, etc.) excepto espacios en blanco.

palabra = input("Input: ")  #abc
dic = {}
palabra = palabra.lower()
for letra in palabra:
    if letra != " ":
        dic[letra] = palabra.count(letra)  # dic["a"] = 1

print(dic)

