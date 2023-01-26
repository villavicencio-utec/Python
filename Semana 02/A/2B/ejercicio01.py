# kw = int(input("kw:"))  # 120
# condicion  = kw <= 100  # False
#
# monto_1 = (kw * 0.4522)*condicion #  (kw * 0.4522)*0
# monto_2 = (0.4522 * 100 + (kw - 100) * 0.7)*(not condicion)  # (0.4522 * 100 + (kw - 100) * 0.7)*1
#
# monto = monto_1 + monto_2 # 0 + resultado
# print("El monto a pagar es:", round(monto,2))


consumo_kW = int(input("Kw:"))

tarifa1 = 0.4522
tarifa2 = 0.7

limite = 100

consumo_en_soles = (consumo_kW <= limite) * (tarifa1 * consumo_kW) + (consumo_kW > limite) * (tarifa1 * limite + tarifa2 * (consumo_kW - limite))

print("El consumo en soles es: ", consumo_en_soles)



