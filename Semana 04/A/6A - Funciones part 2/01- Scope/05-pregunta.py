y = 8

def mystery(x):
    s = 0
    for i in range(x):
        x = i+1
        s = s + x

    return s

def main():
    x = 4
    x = mystery(x+1)
    print(4)


