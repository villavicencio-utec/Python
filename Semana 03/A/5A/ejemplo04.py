numero = int(input("Numero [mayor a 15]: "))   # 20
while numero < 15:
    numero = int(input("Numero [mayor a 15]: "))

i = 1
while numero >= i:  # 20 >= 2  -> True
    j = 1
    fact = 1
    while i >= j:  # 3>=4
        fact = fact*j  # 1*1*2*3  = 3!
        j += 1

    print(i, fact)
    i += 1

