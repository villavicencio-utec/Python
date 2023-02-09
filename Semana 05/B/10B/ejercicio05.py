# 5. Desarrollar un programa en Python que permita ingresar “N” DNIs a un diccionario
# (se termina de ingresar con un DNI = -1). Al terminar debe mostrar el DNI con el máximo valor.
# Validar que el DNI debe tener 8 dígitos, sino mostrar el mensaje DNI INCORRECTO.
# Recordar cada DNI ingresado debe ser único.
def validarDNI(dni):
    if len(dni) == 8:
        return True
    else:
        return False


dic = {}
i = 1
dni  = input("DN1 {}: ".format(i))
if not validarDNI(dni):
    i = 1
    print("DNI INCORRECTO")

dni = int(dni)
mayor = dni
dic[dni]= i
while dni != -1:

    dni  = input("DN1 {}: ".format(i))

    if not validarDNI(dni):
        print("DNI INCORRECTO")
    else:
        dni = int(dni)
        i += 1
        if dni > mayor:
            dic[dni]= i
            mayor = dni


print("El DNI con mayor valor es: " ,mayor)


