import math
n = int(input())
ras = 0
for i in range(0, n):
    ras += 1 / math.factorial(i)
print('%.4f' % ras)