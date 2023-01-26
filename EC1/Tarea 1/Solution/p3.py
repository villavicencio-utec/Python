PH=int(input("Ingrese el PH: "))
if (PH>=0) and (PH<2):
    print("Muy ácido")
    print("\nGracias por usar el programa! ")

elif(PH>=2) and (PH<5):
    print("Moderadamente ácido")
    print("\nGracias por usar el programa! ")

elif(PH>=5) and (PH<7):
    print("Ligeramente ácido")
    print("\nGracias por usar el programa! ")

elif(PH>=7) and (PH<8):
    print("Neutro")
    print("\nGracias por usar el programa! ")

elif(PH>=8) and (PH<10):
    print("Ligeramente básico")
    print("\nGracias por usar el programa! ")

elif(PH>=10) and (PH<13):
    print("Moderadamente básico")
    print("\nGracias por usar el programa! ")

elif(PH>=13) and (PH<=14):
    print("Muy básico")
    print("\nGracias por usar el programa! ")

else:
    print("El valor esta fuera del rango :(")

