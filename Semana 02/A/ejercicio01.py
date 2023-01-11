kw = int(input("kw:"))
if kw <= 100:
    monto = kw * 0.4522
else:
    monto = 0.4522 * 100 + (kw - 100) * 0.7

print("El monto a pagar es:", monto)