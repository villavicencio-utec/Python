#inmutable
def funcion1(a, b): # a= 1,  b = 2
    a = a + 1 # a = 2
    b = b * 5 # b = 10
    return a, b


def funcion2(a, b): # a= 1,  b = 2
    a = a + 1 # a = 2
    b = b * 5 # b = 10

x = 1
y = 2
print("Antes de la funcion",x,y)
x, y = funcion1(x,y) # parametros por valor example int, float y bool
print("Despues de la funcion",x,y)




