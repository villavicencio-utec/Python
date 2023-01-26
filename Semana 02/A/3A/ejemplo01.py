nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Hola " + nombre)
print("Hola", nombre)
print("Hola {} , {} ".format(nombre, edad))
print(f"Hola {nombre}")

if edad == 18:
    print("Usted debe tramitar ante el RENIEC su DNI mayor de edad.")
