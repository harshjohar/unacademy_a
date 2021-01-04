n = int(input())
m = int(input())

for i in range(n):
    result = 0
    for i in range(m):
        marks = int(input())
        result += marks
    print(result/m)