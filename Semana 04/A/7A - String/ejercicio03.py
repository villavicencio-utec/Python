palabra = input("Ingresa palabra: ")  # HoLa
nueva = ""

for i in range(len(palabra)):
    if i % 2 == 0:  # par
        nueva = nueva + palabra[i].upper()  # "" + H = "H"
    else:  # impar
        nueva += palabra[i].lower()  # "H" + "o" = "Ho"
        # nueva = nueva + palabra[i].lower()  # "H" + "o" = "Ho"


print(nueva)
