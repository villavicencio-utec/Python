denominacion = int(input("Ingrese denominacion: "))

if denominacion == 1:
    personaje = "George Washington"
elif denominacion == 2:
    personaje = "Thomas Jefferson"
elif denominacion == 5:
    personaje = "Abraham Lincoln"
elif denominacion == 10:
    personaje = "Alexander Hamilton"
elif denominacion == 20:
    personaje = "Andrew Jackson"
elif denominacion == 50:
    personaje = "Ulysses S. Grant"
elif denominacion == 100:
    personaje = "Benjamin Franklin"
elif denominacion == 500 or denominacion == 1000 or denominacion ==  5000 or denominacion ==  10000:
    personaje ="Denominación descontinuada"
else:
    personaje = "No existe esa denominación"


print(personaje)
