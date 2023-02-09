# lista = [expresion for item in iterable ]
# lista = [expresion for item in iterable if condition]

numeros = [1,2,3,4,5,6,7,8]
r1 = []
for item in numeros:
    valor = item*2
    r1.append(valor)

print(r1)

#Comprension de lista.
r2 = [e*2 for e in numeros]
print(r2)



strings = ["Domingo","Lunes","Martes"]

r3 = []
for dia in strings:
    valor = dia.upper()
    r3.append(valor)
print(r3)

r4 = [e.upper() for e in strings]

print(r4)











