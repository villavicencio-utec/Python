lista_letras = ['a', 'b', 'c', 'd', 'e']
variable = 'Hola'
posicion = -1

if variable in lista_letras:  # Verifico que se encuentre dentro de la liste
    posicion = lista_letras.index(variable)  # pido el indice
    print("Esta es la posicion:", posicion)
else:
    print("No hay elemento en la lista")
