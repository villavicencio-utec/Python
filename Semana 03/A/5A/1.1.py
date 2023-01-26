#tam = int(input("Ingrese el tamanho: "))
tam=8
filas=1

while filas <=tam:
   columnas = 1
   while columnas<=filas:
       print("# ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas=1
while filas <=tam:
   columnas = 1
   while columnas <= tam - filas + 1:
       print("# ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas=1
while filas <=tam:
   columnas = 1
   while columnas<= tam:
       if filas <= columnas:
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas=1
while filas <=tam:
   columnas = 1
   while columnas<= tam:
       if filas < tam-columnas+1:
           print("  ", end="")
       else:
           print("# ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas = 1
while filas <= tam:
   columnas = 1
   while columnas <= tam:
       if filas ==1 or filas == tam or columnas ==1 or columnas == tam :
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas = 1
while filas <= tam:
   columnas = 1
   while columnas <= tam:
       if filas ==1 or filas == tam or filas== columnas:
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1


print("----------------")

filas = 1
while filas <= tam:
   columnas = 1
   while columnas <= tam:
       if filas ==1 or filas == tam or filas== tam - columnas +1 :
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas = 1
while filas <= tam:
   columnas = 1
   while columnas <= tam:
       if filas ==1 or filas == tam or filas== columnas or filas== tam - columnas +1 :
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1

print("----------------")

filas = 1
while filas <= tam:
   columnas = 1
   while columnas <= tam:
       if filas ==1 or filas == tam or columnas ==1 or columnas == tam or filas== columnas or filas== tam - columnas +1 :
           print("# ", end="")
       else:
           print("  ", end="")
       columnas = columnas + 1
   print("")
   filas = filas + 1