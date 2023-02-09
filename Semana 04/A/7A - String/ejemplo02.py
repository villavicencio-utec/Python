frase = "Estamos desarrollando un codigo en python"
letra = "e"
# letra1 = "o"
# letra2 = "e"
cantidad = 0

for i in frase:  # s
    if letra == i:  # "s" == "s"
        cantidad += 1

print("La letra", letra, "aparece", cantidad, "en la frase", frase)