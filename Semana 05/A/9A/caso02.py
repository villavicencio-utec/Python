
d1 = []
d2 = []

def crearDigitos():
    global d1, d2,d4
    d1 =[[' ',' ','x',' ',' '],
         [' ','x','x',' ',' '],
         ['x',' ','x',' ',' '],
         [' ',' ','x',' ',' '],
         [' ',' ','x',' ',' '],
         [' ',' ','x',' ',' '],
         ['x','x','x','x','x']]

    d2 = [['x','x','x','x','x'],
          [' ',' ',' ',' ','x'],
          [' ',' ',' ',' ','x'],
          ['x','x','x','x','x'],
          ['x',' ',' ',' ',' '],
          ['x',' ',' ',' ',' '],
          ['x','x','x','x','x']]

    d4 = [['x',' ',' ',' ','x'],
          ['x',' ',' ',' ','x'],
          ['x',' ',' ',' ','x'],
          ['x','x','x','x','x'],
          [' ',' ',' ',' ','x'],
          [' ',' ',' ',' ','x'],
          [' ',' ',' ',' ','x']]

def mostrarDigito(digito):
    print('')
    for i in range(len(digito)):
        for j in range(len(digito[0])):
            print(digito[i][j],end=' ')
        print('')


def mostrarDigitoGrupal(digitos):
    print('')
    for digito in digitos:
        for i in range(len(digito)):
            for j in range(len(digito[0])):
                print(digito[i][j],end=' ')
            print('')

crearDigitos()
mostrarDigito(d2)

digitos = []
digitos.append(d1)
digitos.append(d2)
digitos.append(d4)

print(digitos)

mostrarDigitoGrupal(digitos)
