s1 = input("Ingrese string s1: ")  # Jorge
mayusculas = ""
minusculas = ""

for i in s1:
   if i.islower():  # True si es minuscula
       minusculas = minusculas + i
   else:
       mayusculas = mayusculas + i


# recorrido por indice
# for i in range(len(s1)):
#     print(s1[i])

print(minusculas)
print(mayusculas)

