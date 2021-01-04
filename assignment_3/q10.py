h = int(input())

def factorial(i):
    result = 1
    for i in range(1, i+1):
        result *= i
    return result

def ncr(n, r):
    answer = (factorial(n))/((factorial(n-r))*(factorial(r)))
    return int(answer)

for i in range(h+1):
    for space in range(h - i, 0, -1):
        print(' ', end='')
    for j in range(i+1):
        print(ncr(i, j), end='  ')

    print()
    
    