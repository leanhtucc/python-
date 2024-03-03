from math import *
def check(n):
    rev = n % 10
    while n != 0:
        if n % 10 > rev:
            return False
        n //= 10
    return True

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
dem = 0
for i in range(n + 1):
    if check(i) and prime(i):
        print(i, end = ' ')
        dem += 1
print('\n', dem, sep = ' ')