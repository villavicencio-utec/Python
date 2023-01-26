
agua_ml = int(input("Ingrese la cantidad de agua a embotellar(ml): "))
botellas_20l = agua_ml // 20000
residuo = agua_ml % 20000

botellas_7l = residuo // 7000
residuo = residuo % 7000

botellas_2l = residuo // 2000
residuo = residuo % 2000

botellas_600ml = residuo // 600
residuo = residuo % 600

print("Unidades de presentación de 20l: ", botellas_20l)
print("Unidades de presentación de 7l: ", botellas_7l)
print("Unidades de presentación de 2l: ", botellas_2l)
print("Unidades de presentación de 600ml: ", botellas_600ml)
print("residuo: ", residuo)
