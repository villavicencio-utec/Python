PAISES = 11 #fila
AÑOS = 2 # Columna
paises = [ "Argentina", "Bolivia", "Brasil", "Chile", "Colombia",
          "Ecuador", "Mexico", "Paraguay", "Perú", "Uruguay",
          "Venezuela"]
pbi = [ [2.9 , 2.5], [3.9 ,  4.0], [0.9 ,  2.2],[1.5 , 3.3],
        [1.8 , 2.6], [1.0 , 2.0],  [2.2 , 2.3], [4.0 , 4.0],
        [2.5 , 3.5], [3.0 , 3.0], [-9.5 , -8.5] ] # matriz

for i in range(PAISES): # i  = 1
    for j in range(AÑOS): # j = 0
        print(pbi[i][j],  end="   ") #pbi[0][1]
    print()

# for i in range(PAISES): #FILAS   i = 0 , 1, 2, 3 .... 10
#     # print("%10s"%paises[i], end="   ")
#     for j in range(AÑOS): # COLUMNAS   j = 0, 1
#         print("{0:.1f}".format(pbi[i][j]), end=" ")  # pbi[0][1]
#     print()


# matriz[i][j]

#
#
#
# #Imprimir por medio de Tabulate
# print(tabulate(pbi, headers=["2017", "2018"]))