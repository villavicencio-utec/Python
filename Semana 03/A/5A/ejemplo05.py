filas = int(input("Filas: "))  #5
while filas <1 or filas >9:
    filas = int(input("Filas: "))

f=1
while  filas >= f:   # 5>=1  5>=2 .... 5>=5 5>=6
   c = 1
   while  filas >= c:
       if f > filas-c:
           print(filas - c + 1 , end="")
       else:
           print(0, end="")
       c += 1
   print("")
   f = f + 1
