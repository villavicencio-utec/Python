def f(a):
    return 3*a + 5 # 305

def g(b): # b 10
    return b**2

numero = int(input("Ingrese un valor para x: ")) # 10
resultadoG = g(numero) #100
res = f(resultadoG)
print("El valor de la función compuesta es:", res)



