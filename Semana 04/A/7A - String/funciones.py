# str
pi = 3.14
texto = "El valor de pi es " + str(pi)
print("El valor de pi es " + str(pi))

#len
palabra = "aeiou          "
print(len(palabra))

vocales = "Hola mundo, como estas"
print(vocales.find("z"))
print(vocales.find("como"))

palabras = "Variables globales y variables locales"
palabras = palabras.replace("a", "A")
print(palabras)
#
cadena2 = "hoy dia se estrena doctor Strange"
cadena = "  Hoy dia se eStrena doctor StrAnge   "
print(cadena2.capitalize())
print(cadena.lower())
print(cadena.upper())
print(cadena.strip())
#
#
palabra = "Hola"
print("...".join(palabra))
