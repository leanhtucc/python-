import math
n = int(input())
gt = 1
sum =0
for i in range(1, n+1):
    gt *= i
    sum += gt
print(sum)