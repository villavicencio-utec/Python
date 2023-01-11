numero = int(input("Numero: ")) #104
a = numero % 10  #4
numero = numero//10 # 10

b = numero % 10 # 0
numero = numero//10 # 1

c = numero % 10 # 1
numero = numero//10 # 0
resultado = a*100 + b*10 + c
print("Numero invertido:", resultado)
