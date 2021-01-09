d = int(input())
arr = []

for i in range(d):
    c = int(input())
    arr.append(c)

count = 0

for j in range(d-1):
    if arr[j] * arr[j+1] < 0:
        count += 1

print(count)