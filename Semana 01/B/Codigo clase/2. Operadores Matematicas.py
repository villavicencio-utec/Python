print("Suma\n")
# Suma
x = 10 + 9
print(x, type(x)) # int

x = 10 + 9.0
print(x, type(x)) # float

x = 10 + float("5")
print(x, type(x))

x = 10 + False
print(x, type(x))

x = "Jorge" + " " + "Pyhton" + " " + "M603"  # concatenar
print(x, type(x)) # 1010 - string

print()
print("Resta\n")
# Resta
x = 10 - 9
print(x, type(x)) # 1 - int

x = 10 - 9.0
print(x, type(x)) # 1.0 float

x = 10 - int("5")
print(x, type(x)) # 5 int

x = 10 - True
print(x, type(x)) # 9 - int

print()
print("Multiplicacion\n")
# Multiplicacion
x = 10 * 9
print(x, type(x)) # 90 - int

x = 10 * 9.0
print(x, type(x)) # 90.0 float


x = 10 * True
print(x, type(x)) # 10 int

x = 10 * False
print(x, type(x)) # 0 float


x = "Hola"*5
print(x, type(x)) # "1010101010" - str


x = "Hola"*10
print(x, type(x))



print()
print("Division\n")
# Division decimal /
x = 95/10.0
print(x, type(x)) # 9.5 - float

# Division entera //
x = 95//10.0
print(x, type(x)) # 9 - int

x = 86/True
print(x, type(x))

print()
print("Potencia\n")
# Potencia
x = 10 ** 2
print(x, type(x)) # 100 - int

x = 10.7 ** 2
print(x, type(x))  # 114.48999999999998 - int

x = False ** 2
print(x, type(x))


print()
print("Residuo\n")
# Residuo  %
x = 26 % 5
print(x, type(x))

x = 5 % 10
print(x, type(x))

# Raiz
x = 32 ** 0.2
print(x, type(x))


# Precedencia de operadores

print("\nPrecedencia de operadores")
x = 3 * 5 + 1
print(x)

x = (3 + 5) * 2
print(x)


x = 3 + 5 * 2 - 10**2
print(x)

x = 10 - 5 + 12 - 9 + 6
print(x)
