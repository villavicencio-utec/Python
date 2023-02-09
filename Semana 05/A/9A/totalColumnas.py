TRIMESTRES = 3  # columnas
DIVISIONES = 5  # filas

suma = 0
divisiones = ["Línea Blanca", "Electrodomésticos", "Juguetería",
              "Perecibles", "Limpieza"]
datos = [[450, 650, 342], [340, 487, 767], [134, 212, 354],
         [180, 464, 565], [647, 324, 232]]  # matriz es una lista de listas

COL_constante = 2
for i in range(0, DIVISIONES, 2):
    suma = suma + datos[i][COL_constante]


print("\nEl total de ventas del segundo Trimestre es: ", suma)
