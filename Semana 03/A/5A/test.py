n = int(input())
m = int(input())

if n == 0 or m == 0:
    print("La tabla es nula")
elif n < 0 or m < 0:
    print("No se permiten numeros negativos")
else:
    i = 1
    while i <= m:
        mult = i * n
        print("{}*{}={}".format(i, n, mult))
        i += 1
