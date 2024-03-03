from math import *
def check(n):
    tempt = n
    rev = 0
    tong = 0
    ok =False
    while n != 0:
        rev = rev * 10 + n % 10
        if n % 10 == 6:
            ok = True
        tong += n % 10
        n //= 10
    return ok and (tempt == rev) and (tong % 10 ==8)


a, b = map(int, input().split())
for i in range(a, b + 1):
    if check(i):
        print(i, end = ' ')