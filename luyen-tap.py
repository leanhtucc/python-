from math import *
#1
def prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1
#2
def sum(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong
#3
def sum_even_number(n):
    tong = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            tong += n % 10
        n //= 10
    return tong
#4
def sum_prime(n):
    tong = 0
    while n != 0:
       r = n % 10
       if r == 2 or r == 3 or r == 5 or r == 7:
            tong += r
            n //= 10
    return tong
#5
def flipped_number(n):
    tong = 0
    while n != 0:
        tong = tong * 10 + n % 10
        n //= 10
    return tong
#6
def number_of_prime_divisors(n):
    dem = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            dem += 1
            while n % i == 0:
                n //= i
    if n > 1:
        dem += 1
    return dem
#7
def greatest_prime_divisor(n):
    res = -1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res = i
            while n % i == 0:
                n //= i
    if n > 1:
        res = n
    return res
#8
def kiem_tra(n):
    while n != 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
#9
def sum_2(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    if tong % 8 ==0:
        return 1
    else:
        return 0
#10
def sum_mathematics(n):
    tong = 0
    while n != 0:
        tong += factorial(n % 10)
        n //= 10
    return tong
#11 kiem tra n co phai chi tao tu 1 so
def test(n):
    dv = n % 10
    while n != 0:
        if dv != n %10:
            return 0
        n //= 10
    return 1
#12 kt n co chu so tan cung lon nhat hay khong
def test_2(n):
    dv = n % 10
    while n != 0:
        if n % 10 > dv:
            return 0
        n //= 10
    return 1
#13 in tong luy thua chu so cua n voi so mu la so chu so
def test_3(n):
    m = n
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    tong = 0
    while m != 0:
        tong += (m % 10) ** cnt
        m //= 10
    return tong
if __name__ == '__name__':
    n =int(input())