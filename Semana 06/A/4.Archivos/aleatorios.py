# w write = escritura
# r read = lectura
# w+ write + read = ambos
import random as rd
archivo = open("jorge.txt", "w")  # 1.apertura del archivo

cantidad = int(input("Ingresar cantidad de numeros aleatorios: "))
for i in range(cantidad):
    valor = rd.randint(1, 20)
    archivo.write(str(valor) + "\n")

archivo.close()  # 3. Cerrar archivo
