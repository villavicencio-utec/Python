# Escribir un programa en Python que permita ingresar un monto en soles y muestre su equivalente en dólares y euros.


monto = float(input("Ingresar monto en soles: "))
dolares = monto * 0.27
euros = monto * 0.24
print("El monto", monto, "en dolares es", dolares)
# print("El monto", monto, "en dolares es", euros)
print("El monto {} en dolares es {}".format(dolares, euros))
