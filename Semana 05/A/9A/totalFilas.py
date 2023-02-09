TRIMESTRES = 3  # columnas
DIVISIONES = 5  # filas

suma = 0


divisiones = ["Línea Blanca", "Electrodomésticos", "Juguetería",
              "Perecibles", "Limpieza"]
datos = [[450, 650, 342], [340, 487, 767], [134, 212, 354],
         [180, 464, 565], [647, 324, 232]]  # matriz es una lista de listas

Cons_FILA = 3
for j in range(TRIMESTRES):
    suma = suma + datos[Cons_FILA][j]
    # datos[3][0]
    # datos[3][1]
    # datos[3][2]
    # datos[3][3]

print("\nEl total de ventas de la División Juguetería es: ",suma)
