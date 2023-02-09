balance = 10000  # --- variable global
dias_semana = 7
meses_anio = True
valor_global = "Soy un string"
flotante_global = 10.3

def actualizar_global(amount):
    global balance  # -- esta funcion intenta
    # actualizar el valor de la
    # variable global balance
    if balance >= amount:
        balance = balance - amount

    print(balance)


def globales():
    print(balance)


# globales()
actualizar_global(50)



