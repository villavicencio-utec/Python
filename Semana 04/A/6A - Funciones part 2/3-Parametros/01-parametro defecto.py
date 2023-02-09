def estudiante(nombre, apellido="Mark", standard="Quinto", numero=20):
    print(nombre, apellido, " estudia en ", standard, "standard", "edad", numero)


# --- 1 parametro posicional
estudiante("John")
#
# --- 3 parametros posicionales
estudiante("John", "Gates", "7", 14)

# # --- 2 parametros posicionales
estudiante("John", "Gates")
estudiante("John", "Setimo")

