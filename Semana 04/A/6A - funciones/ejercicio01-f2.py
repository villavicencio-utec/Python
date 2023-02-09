def funcionCompuesta(x):
    g = pow(x,2)
    f = 3*g + 5
    return f

x = int(input("Ingrese un valor para x: "))
res = funcionCompuesta(x)
print("El valor de la función compuesta es:", res)



