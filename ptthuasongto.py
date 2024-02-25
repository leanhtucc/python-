import math
def pt(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                print(i,end='')
                n //= i
    if n > 1:
        print(n)
n = int(input())
print(pt(n))