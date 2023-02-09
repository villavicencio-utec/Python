s1 = input("Ingrese string s1: ") #hola
s2 = input("Ingrese string s2: ")  #adios

medio = len(s1)//2
print(medio)

s3 = s1[:medio] + s2 + s1[medio:]
print(s3)

