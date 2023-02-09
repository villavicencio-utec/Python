def f(x):
    return  g(x) + h(x)

def g(x):
    return 4*h(x)

def h(x):
    return x**2

print(f(2))


#f(2) =  g(2) + h(2)  = 16 + 4 = 20
#g(2) =  4*h(2) = 4*4 = 16
#h(2) = 2**2 = 4




