# 3 4 5
# 7 7 7
# 2 2 5

lado1= int(input('Lado 1 : '))
lado2= int(input('Lado 2 : '))
lado3= int(input('Lado 3 : '))

equilatero= (lado1+lado2+lado3)/3

s= (lado1+lado2+lado3)/2
area= (s*(s-lado1)*(s-lado2)*(s-lado3))**0.5

if lado3 == 0:
    print('No se puede formar un triangulo')
elif lado1+lado2 > lado3:
    print('Es un triangulo')
    if equilatero == lado1:
        print('Triangulo equilatero')
    elif lado1 ==lado2:
        print('Es triangulo isosceles')
    elif lado2 == lado3:
        print('Es triangulo isosceles')
    elif lado1 == lado3:
        print('Es triangulo isosceles')
    else:
        print('Es triangulo escaleno')
    print('El area es: ', area)
else:
    print('No se puede formar un triangulo')
