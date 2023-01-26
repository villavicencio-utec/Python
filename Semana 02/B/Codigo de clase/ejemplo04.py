# Diseñe e implemente un algoritmo que imprima los números pares
# del 8 al 0, pero si se detecta el número 4, que acabe el bucle y muestre el mensaje “while terminado.”

i = 10
while i >= 0:  # 6 >= 0  -> True
    i = i - 2  # i = 4
    if i == 4:  # 4 == 4 -> True
        break
    print(i)  # 8 , 6

print("while terminado")


