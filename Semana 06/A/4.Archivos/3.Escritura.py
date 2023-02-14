# w write = escritura
# r read = lectura
# w+ write + read = ambos
inputFile = open("jvillavicencio.txt", "w")  # 1.apertura del archivo

inputFile.write("Jorge Villavicencio\n")  # 2. Escribir texto
inputFile.write("Los olivos")

inputFile.close()  # 3. Cerrar archivo
