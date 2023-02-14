#Modo binario solo para windows.
# r – Lectura únicamente.
# w – Escritura únicamente, reemplazando el contenido actual del archivo o bien creándolo si es inexistente.
# a – Escritura únicamente, manteniendo el contenido actual y añadiendo los datos al final del archivo.
# w+, r+ o a+ – Lectura y escritura.

# El signo '+' permite realizar ambas operaciones.
# La diferencia entre w+ y r+ consiste en que la primera opción borra el contenido anterior antes de escribir nuevos datos,
# y crea el archivo en caso de ser inexistente. a+ se comporta de manera similar,
# aunque añade los datos al finaldel archiv

archivo = open("prueba.txt", "r")
# print(archivo)
for oracion in archivo:
    print(oracion)


# listaPokemon = open("pokemon_list.txt","r")
# listaPokemon = open("pokemon_list.txt","a") #agregar
# listaPokemon = open("pokemon_list.txt","w") # escritura
# listaPokemon = open("pokemon_list.txt","rb")
# listaPokemon = open("pokemon_list.txt","rb+")
# listaPokemon = open("pokemon_list.txt","w")
# listaPokemon = open("pokemon_list.txt","wb")
# listaPokemon = open("pokemon_list.txt","w+")
# for palabra in listaPokemon:
#     print(palabra)