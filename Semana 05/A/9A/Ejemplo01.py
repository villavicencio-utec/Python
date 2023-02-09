PAISES = 14
DATOS = 6
paises = ["Costa Rica", "Argentina", "Panamá", "Chile", "Uruguay",
          "Paraguay", "Colombia", "Perú", "Ecuador", "Bolivia", "Brasil",
          "México", "Nicaragua", "Venezuela"]
datos = [[2290, 569, 4, 300255, 527.7, 131],
         [75, 22.8, 3.3, 9500, 416.7, 127],
         [5.9, 1, 5.9, 744, 744, 126],
         [2600, 634, 4.1, 276000, 435.3, 106],
         [140, 30.8, 4.5, 13430, 436, 96],
         [26542, 5601, 4.7, 2200000, 392.8, 83],
         [10900, 2964, 3.7, 869453, 293.3, 80],
         [11.5, 3.3, 3.5, 850, 257.6, 74],
         [5.5, 1, 5.5, 386, 386, 70],
         [34, 7, 4.9, 2000, 287.4, 59],
         [16.5, 3.6, 4.6, 965, 268.1, 58],
         [48, 19.6, 2.5, 2687, 137.2, 56],
         [168, 31.3, 5.4, 8445, 269.6, 50],
         [168000, 690854, 0.2, 1308000, 1.9, 8]]

# imprimir matriz
for i in range(PAISES):  # Filas i = 0 ....13
    print("%10s" % paises[i], end="   ")

    for j in range(DATOS):  # Columnas  j = 0 ... 5
        print("%12.4f" % (datos[i][j]), end=" ")  # (datos[0][0]) (datos[0][1]) ... (datos[0][5])
        # print((datos[i][j]), end=" ")  # (datos[0][0]) (datos[0][1]) ... (datos[0][5])
    print()

#
# a

# pais = input("\nIngrese país: ")
# pos = -1
# if pais in paises:
#     pos = paises.index(pais)  # 1
#     for j in range(DATOS):  # Columnas
#         print("%15d" % datos[pos][j], end="  ")  # (datos[1][0]) (datos[1][1]) ... (datos[1][5])
# else:
#     print("País no se encuentra en la lista")

#
# b
# suma = 0
#
# for i in range(PAISES):
#     suma = suma + datos[i][5]  # datos[0][5] + datos[1][5] ... + datos[13][5]
# print("\nLa cantidad total de BigMacs es:", suma)

#
# c
print("Los países con ingreso mínimo superior a 100 dólares son:")
for i in range(PAISES):
    if datos[i][5] < 50:
        print(paises[i], end=" ")
