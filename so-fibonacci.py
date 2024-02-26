import math
def fibonacci(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print('0,1', end = ' ')
        fn1, fn2 = 1, 0
        for i in range(2, n -1):
            fn = fn1 + fn2
            fn2, fn1 = fn1, fn
for i in range(int(input())):
    n = input()
    print(fibonacci(n))