import math
def gcd(a, b):
    while b != 0:
        a, b= b, a%b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
print(gcd(18, 15))
print(lcm(18, 15))
a, b, c = 10, 20, 35
print(gcd(gcd(a,b), 35))