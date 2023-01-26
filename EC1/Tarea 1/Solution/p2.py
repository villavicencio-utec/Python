# 9 30 0
# 18 30 12

t1_hrs = int(input("Ingrese las horas del tiempo 1: "))
t1_min = int(input("Ingrese los minutos del tiempo 1: "))
t1_sec = int(input("Ingrese los segundos del tiempo 1: "))

# Input: tiempo 2
t2_hrs = int(input("Ingrese las horas del tiempo 2: "))
t2_min = int(input("Ingrese los minutos del tiempo 2: "))
t2_sec = int(input("Ingrese los segundos del tiempo 2: "))

t1_sec += t1_min * 60 + t1_hrs * 3600
t2_sec += t2_min * 60 + t2_hrs * 3600
transcurrido_sec = t2_sec - t1_sec

transcurrido_hrs = transcurrido_sec // 3600
transcurrido_min = (transcurrido_sec % 3600) // 60
transcurrido_sec = transcurrido_sec % 60

print("Tiempo transcurrido: {} horas, {} minutos, {} segundos".format(transcurrido_hrs, transcurrido_min, transcurrido_sec))
