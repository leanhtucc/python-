from math import *
def cp(n):
    can = isqrt(n)
    if can * can == n:
        return True
    else:
        return False
a, b = map(int, input().split())
can1, can2 = isqrt(a), isqrt(b)
if can1 * can1 != a:
    can1 += 1
if (can2 + 1) * (can2 + 1) == b:
    can2 += 1
print(can2 - can1 + 1)