segundos = int(input("Segundos:"))
dias = segundos//86400
segundos = segundos % 86400

horas = segundos//3600
segundos = segundos % 3600

minutos = segundos//60
seg = segundos % 60

print("Equivale a: {}:{}:{}:{}".format(dias, horas, minutos, seg))

