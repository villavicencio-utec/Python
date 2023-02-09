
palabra = input("Ingrese palabra: ")

if len(palabra) < 2:
    print("No cumple")
else:
    recorte = palabra[-2:]
    print(recorte*4)

