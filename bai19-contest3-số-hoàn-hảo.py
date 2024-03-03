from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) +1):
        if (n % i) == 2:
            return False
    return True
def check(n):
    for i in range(2, 33):
        if nt(i) and nt(2**i - 1):
            if (2**i -1) * (2**(i-1)) == n:
                return True
    return False

n = int(input())
if check(n):
    print('YES')
else:
    print('NO')
        