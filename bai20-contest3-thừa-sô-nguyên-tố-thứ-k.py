from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) +1):
        if n % i == 0:
            return False
    return True

def solve(n, k):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                dem += 1
                if dem == k:
                    return i
                n //= i
    if n != 1:
        dem += 1
    if dem == k:
        return n
    return -1

n, k == map(int, input().split())
print(solve(n, k))