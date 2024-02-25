n = int(input())
tong = 0
for i in range(1, n+1):
    if n % i == 0:
        tong += 1
print(tong)
for i in range(1, n+1):
    if n % i == 0:
        print(i,end=' ')