PAISES = 5  # FILAS
TIPOS_MEDALLA = 3  # COLUMNAS
nombres_paises = ["Estados Unidos", "Unión Soviética", "Reino Unido",
                  "China", "Alemania"]
medallas = [
    [1022, 794, 704], [395, 319, 296], [263, 295, 289],
    [227, 163, 153], [219, 246, 269]
]
print("%17s"%" ", "%6s"%"ORO","%6s"%"PLATA","%6s"%"BRONCE")
# print("\t\t\tORO  PLATA  BRONCE")
for i in range(PAISES):  # Recorrido de FILAS
    print("%17s" % nombres_paises[i], end=" ")
    for j in range(TIPOS_MEDALLA):  # Recorrido de Columnas
        print("%6d" % medallas[i][j], end=" ")
    print()

# a
# total = 0
# for j in range(TIPOS_MEDALLA):
#     total = total + medallas[3][j]
#     # total = 0 + medallas[3][0] = 0 + 227
#     # total = 227 + medallas[3][1]  = 227 + 163 = 390
#     # total = 390 + medallas[3][2] = 390 +  153 = 543
#
# print("\nEl total de medallas de China: ", total)

# b
# total = 0
# for i in range(PAISES):
#     total = total + medallas[i][2]
#
# print("\nEl total de medallas de bronce: ", total)

# # c
suma = 0
for i in range(PAISES):
    for j in range(TIPOS_MEDALLA):
        suma = suma + medallas[i][j]

print("\nLa cantidad total de medallas es: ", suma)
