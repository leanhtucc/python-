import math
def square(n):
    can = math.isqrt(n)
    return can * can == 0

def cube(n):
    can = int(math.pow(n, 1/3))
    return can ** 3 == n or ((can + 1) ** 3 == n)
n = int(input())
if cube(n):
    print('YES')
else:
    print('NO')
