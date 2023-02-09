# El operador = no copia una lista a otra.
# Este operador lo que hace es crear una variable que referencie a los mismos datos.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_punteros = lista
print("Inicialmente", lista_punteros)
lista[2] = 200
lista[4] = 400
print("Luego de la modificacion", lista_punteros)
