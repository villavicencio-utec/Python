frase = input("Ingrese una frase: ")  # Python
n = int(input("Ingrese posición de corte:"))  # 2

if len(frase) > n:
    a = frase[:n]  # frase[:2] Py
    b = frase[n:]  # thon
    print(a, b)

else:
    print("")
