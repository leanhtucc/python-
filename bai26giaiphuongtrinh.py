import math
a, b, n = map(int, input().split())
check = False
for x in range(0, n // a+1):
    temp = n - a*x
    if temp % b == 0:
        check = True
        break
if check:
    print('YES')
else:
    print('NO')