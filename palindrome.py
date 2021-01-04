n = int(input())

result = 0
tmp = n

while tmp >= 1:
    a = tmp%10
    result = 10*result + (a)
    tmp = tmp//10

if result == n:
    print('YES')
else:
    print('NO')