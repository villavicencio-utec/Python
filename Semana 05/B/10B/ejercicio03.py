# Diseñe e implemente un algoritmo que reciba como dato de entrada un texto,
# y proceda a extraer todas las palabras del texto asociando la cantidad de veces que se repite dicha palabra en el texto.
# Use un diccionario para guardar cada palabra diferente
# y las veces que se repite.

# Haciendo uso de un diccionario, implemente un algoritmo que permita determinar cuántas veces se repite
# cada carácter de un string. Considere que su algoritmo debe considerar cualquier caracter
# (letras, números, símbolos, etc.) excepto espacios en blanco.

frase = input("Input: ")
dic = {}
frase = frase.lower()
for palabra in frase.split(" "):  # Hola como estas Hola como estas Hola como estas
    if palabra in dic:
        dic[palabra] = dic[palabra] + 1
    else:
        dic[palabra] = 1

print(dic)
