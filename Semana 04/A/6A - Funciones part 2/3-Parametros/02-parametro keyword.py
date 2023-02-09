def estudiante(nombre, apellido="Mark", standard="Quinto"):
    print(nombre, apellido, " estudia en ", standard, "standard")


# --- 1 parametro con keyword
estudiante(nombre="John")
estudiante("John")

# --- 2 parametros con keyword
estudiante(nombre="John", standard="setimo")

# --- 2 parametros con keyword
estudiante(apellido="Gates", nombre="John")


