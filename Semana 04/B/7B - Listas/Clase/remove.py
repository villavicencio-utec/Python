print("Ejemplos con REMOVE")
#Si se necesita eliminar la primera ocurrencia de un valor, se utiliza la función remove.
lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(lista_letras)
variable = 'c'
if variable in lista_letras:  # Validar que el elemento a eliminar exista
    lista_letras.remove(variable)
else:
    print("No esta dentro de la lista")

print(lista_letras)
