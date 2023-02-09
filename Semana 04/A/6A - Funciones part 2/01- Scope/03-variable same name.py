def main(a):
   result = square(3) + square(4) + a  # 9 + 16 + 2 = 27
   print(result)

def square(n):
   result = n * n
   return result

a = 10
main(2)

