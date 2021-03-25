def isPrime(n):
    # you are given a number n check if the number is prime or not
    # 1 < n <= 10^9
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True
'''
def Eratosthenes(n):
    # quickly checking of prime
    arr = [True]*n
    return True
'''
def exponent(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

def exponent_recursive(a, b):
    # if not isinstance(a, int) or not isinstance(b, int):
    #     print('Valid values paa yr')
    #     return None
    if b == 0:
        return 1
    if b == 1:
        return a
    # recursive task
    return a*exponent_recursive(a, b-1)

def ex_rec_optimised(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    # recursive task
    task = ex_rec_optimised(a, b//2)
    if b%2 == 0:
        return task*task
    else:
        return task*task*a

n = int(input('Check_Prime: '))
pr_check = isPrime(n)
if pr_check:
    print(n, 'is prime.')
else:
    print(n, 'is not prime.')

print('Exponent: ')
a, b = map(int, input().split())
print('Simple approach ans: ', exponent(a, b))
print('Recursive approach ans: ', exponent_recursive(a, b))
print('Recursive optimised: ', ex_rec_optimised(a, b))
