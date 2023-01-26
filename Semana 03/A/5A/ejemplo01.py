alumnos = int(input("Numero de alumnos: "))
nNotas = int(input("Numero de notas por alumnos : "))
ca = 1
while ca <= alumnos:  # 6 <= 5 -> False
   cn = 1
   suma = 0
   print("\nAlumno %d" %(ca))

   while cn <= nNotas:  # 7
       nota = float(input("Nota %d : " %(cn)))
       
       while nota<0 or nota > 20:
          nota = float(input("Nota %d : " %(cn)))

       suma +=nota
       cn = cn + 1



   promedio = suma/nNotas
   print("El promedio para el alumno numero %d es %7.2f" % (ca,promedio))
   ca = ca + 1
print("Fin.")