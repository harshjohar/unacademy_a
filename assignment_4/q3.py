n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

max_count = 0

for j in range(n):
    count = 0
    for k in range(0, n):
        if arr[j] == arr[k]:
            count += 1
            if count > max_count:
                max_count = count

print(max_count)