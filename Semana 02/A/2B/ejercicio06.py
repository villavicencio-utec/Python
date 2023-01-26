entero = int(input("Numero : "))

digito1 =entero%10
entero = entero//10

digito2 =entero%10
entero = entero//10

digito3 =entero%10
entero = entero//10

digito4 =entero%10

sumatoria = digito4+digito3+digito2+digito1
print(digito4 , "+",digito3,"+",digito2,"+",digito1,"=",sumatoria)