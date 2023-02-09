adicional1 = "ing"
adicional2 = "ly"

palabra = input("Ingrese palabra: ")

if len(palabra) >= 3:
    # if palabra[-3:] == "ing":

    if palabra.find("ing") != -1:
        print(palabra + adicional2)
    else:
        print(palabra + adicional1)
else:
    print(palabra)



