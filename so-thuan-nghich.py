import math
def palin(n):
    rev = 0
    temp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return nev == temp
n = int(input())
print (palin(n))
    