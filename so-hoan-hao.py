import math
def perfect(n):
    tong = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong == n
def prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return 0
    return n > 1
def perfect2(n):
    for p in range(2, 35):
        if primt(p):
            if prime(2**p -1):
                if (2**p -1) * (2** (p -1)) == n:
                    return True
    return False
n = int(input())
print(perfect(n))