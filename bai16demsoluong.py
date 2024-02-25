import math
n = int(input())
if n == 0:
    print(1)
else:
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    print(cnt)  