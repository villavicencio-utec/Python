lado1 = int(input("Lado 1:"))
lado2 = int(input("Lado 2:"))
lado3 = int(input("Lado 3:"))

resultado = (lado1 + lado2) > lado3 and (lado3 + lado2) > lado1 and (lado1 + lado3) > lado2

validacion = (resultado == 1)*"Triangulo correcto" + (resultado != 1)*"Triangulo invalido"
print(validacion)




