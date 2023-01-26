# Desarrolle un programa que lea como dato un número cuyo valor puede ser desde 1
# hasta el 500 y el programa cuente números desde 1 hasta el número que se ingresa como dato,
# pero con las siguientes indicaciones:
#
# Si el número es múltiplo de 4, debe mostrar el número y luego “Tic”
# Si el número es múltiplo de 6, debe mostrar el número y luego “Tac”
# Si el número es múltiplo de 4 y de 6, debe mostrar el número y luego “Tic Tac”
# En cualquier otro caso, solo debe mostrar el número.
flag = False
while not flag:
    n = int(input("Numero [1-500]: ")) #12
    if n >= 1 and n <= 500:
        flag = True


i = 1
while n >= i :  # 12 >= 13
    if i%4 == 0 and i%6 == 0:
        print(i, "TicTac") # 12 Tic Tac
    elif i%4 == 0:
        print(i,"Tic") # 12 Tic
    elif i%6 == 0:
        print(i, "Tac") # 12 Tac
    else:
        print(i) #

    i += 1

#1
#2
#3
#4 Tic
#5
#6 Tac
#...
#12 TicTac



