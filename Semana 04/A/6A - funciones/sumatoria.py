def function(a, b):
    a = a + 1
    b = b * 5
    return a, b


x = 1
y = 2
x, y = function(x, y)
print("Fuera de la funcion", x, y)
# 1, 2
# 2, 10
