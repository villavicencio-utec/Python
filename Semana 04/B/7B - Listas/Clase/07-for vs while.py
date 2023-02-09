lineas = []
print('Ingrese líneas de texto')
print('Ingrese una línea vacía para finalizar.')

linea = input('Su línea: ')
while linea != "":
    lineas.append(linea)
    linea = input("Siguiente línea: ")
print('Sus líneas fueron:')
for linea in lineas:
    print(linea)
