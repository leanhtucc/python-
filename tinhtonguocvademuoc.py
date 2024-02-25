import math
def dem_uoc(n):
    cnt = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    return cnt 
def tong_uoc(n):
    tong = 0
    for i in range(1,math.isqrt(n) +1):
        if n % i == 0:
            tong += i + n //i
    return tong
n = int(input())
print(dem_uoc(n))
print(tong_uoc(n))