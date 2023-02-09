
print("Ejemplos con POP")

#Si se necesita eliminar un elemento por su posición en la lista, se puede ulilizar la función pop.
# Por defecto, pop eliminará el último elemento de la lista y retornará el valor de elemento eliminado.

lista_letras = [ 'a','b','c','d','e','f','g','h','i','j','k','l']
print(lista_letras)
itemEliminado = lista_letras.pop() # eliminado l - [ 'a','b','c','d','e','f','g','h','i','j','k']
print(lista_letras)
# itemEliminado2 = lista_letras.pop() # eliminado k - [ 'a','b','c','d','e','f','g','h','i','j']

print(itemEliminado)