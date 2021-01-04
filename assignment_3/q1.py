n = int(input())
result = 0

for i in range(1, n+1):
    if i%6 == 0 and i%5 != 0:
        result += i
        i += 1
    else:
        i += 1
print(result)