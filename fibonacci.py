import sys

n = int(input())

a = 0
b = 1

print(a, end=', ')
if n == 0:
    sys.exit()
else:
    print(b, end=', ')
    if n == 1:
        sys.exit()
    else:
        for i in range(2, n+1):
            sum = a+b
            a = b
            b = sum
            print(sum, end=', ')

print()