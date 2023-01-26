def comb(n, k):
    result = fact(n)/(fact(k)*fact(n-k))
    return result


def fact(n):  # 7
    factorial = 1
    for i in range(2, (n+1)): # 2,3,4,5,6,7
        factorial = factorial*i
        # i = 2 , 1*2
        # i = 3 , 1*2*3
        # i = 4 , 1*2*3*4
        # i = 5 , 1*2*3*4*5
        # i = 6 , 1*2*3*4*5*6
        # i = 7 , 1*2*3*4*5*6*7
    return factorial


n = int(input("N:"))
k = int(input("k:"))
resultado = comb(n, k)
print("Grupos distintos:",int(resultado))

