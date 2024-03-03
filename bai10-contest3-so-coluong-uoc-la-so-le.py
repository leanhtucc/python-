from math import *
def cp(n):
    can = isqrt(n)
    if can * can == n:
        return True
    else:
        return False
n = int(input())
if cp(n):
    print('YES')
else:
    print('NO')