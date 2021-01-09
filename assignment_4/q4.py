n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

for i in range(n):
    if i%2 != 0:
        print(arr[i], end=' ')

for j in range(n):
    if j%2 == 0:
        print(arr[j], end=' ')