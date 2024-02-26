#(A + B) % C = ((A % C) + (B % C)) % C
#(A - B) % C = ((A % C) - (B % C) + C) % C
#(A * B) % C = ((A % C) * (B % C)) % C
#(A / B) % C = ((A % C) * (B^-1 % C)) % C
#Tinh N! chia du cho 10^9 + 7
import math
a, b, c = map(int, input().split())
res = 1
for i in range(b):
    res *= a
    res %= c
print(res)