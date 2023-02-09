
#DATOS DE ENTRADA
valuta = int(input("Denominación    :"))
#PROCESO Y DATOS DE SALIDA
if valuta == 1 or valuta == 2 or valuta == 5:
    print("Es una moneda")
elif valuta == 10:
    print("Es un billete y aparece Machu Picchu")
elif valuta == 20:
    print("Es un billete y aparece la Ciudadela de Chan Chan")
elif valuta == 50:
    print("Es un billete y aparece el Templo de Chavin de Huantar")
elif valuta == 100:
    print("Es un billete y aparece el sitio Arqueológico del Gran Pajaten")
elif valuta == 200:
    print("Es un billete  y aparece la Ciudad Sagrada de Caral")
else:
    print("La denominación no existe")