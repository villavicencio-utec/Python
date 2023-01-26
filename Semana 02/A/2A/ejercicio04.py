cantidad = int(input("Colores : "))  # 104

cajas24 = cantidad//24
cantidad = cantidad % 24

cajas12 = cantidad//12
cantidad = cantidad % 12

cajas6 = cantidad//6
cantidad = cantidad % 6

sobrante = cantidad

print(cajas24, "cajas de colores de 24")
print(cajas12, "cajas de colores de 12")
print(cajas6, "cajas de colores de 06")
print(sobrante, "colores sobrarian")


