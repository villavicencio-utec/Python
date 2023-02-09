# Dado el siguiente texto:
#
#
# texto = "10, 20, 33, 40, 11, 90"
#
# Escribir un programa que genere una lista con 6 valores numéricos
# incluidos en el texto y luego calcular la suma de aquellos valores
# múltiplos de 10.

texto = "10, 20, 33, 40, 11, 90"
lista = [int(x) for x in texto.split(",")]
print(lista)

# lista_10 = [x for x in lista if x%10 == 0]
# print(lista_10)
suma = sum([x for x in lista if x % 10 == 0])  # [10, 20, 40, 90]
print(suma)
