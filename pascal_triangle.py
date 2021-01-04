def factorial(i):
    result = 1
    for i in range(1, i+1):
        result *= i
    return result

def ncr(n, r):
    answer = (factorial(n))/((factorial(n-r))*(factorial(r)))
    return int(answer)

n = int(input('n: '))
r = int(input('r: '))

e = ncr(n, r)

print(e)