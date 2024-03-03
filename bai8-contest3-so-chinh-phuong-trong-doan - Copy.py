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
for i in range(can1, can2 + 1):
    print(i *i, end = ' ')