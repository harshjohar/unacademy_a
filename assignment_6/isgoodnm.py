# from functools import reduce
# def factors(n):    
#     return set(reduce(list.__add__, 
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# retun a set which contains all the factors of 'n'

def fact_sum(n):
    sum=0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i != n//i:
                sum+=(i+n//i)
            else:
                sum+=i
    return sum-n
n = int(input())
if n == fact_sum(n):
    print('YES')
else:
    print('NO')