from math import *
def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n% i == 0:
            return False
    return True
def check(n):
    tong =0
    while  n != 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        tong += r
        n //= 10
    return prime(tong)


a, b = map(int, input().split())
dem = 0
for i in range(a, b + 1):
    if prime(i) and check(i):
        dem += 1
print(dem)