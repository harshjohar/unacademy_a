n = int(input())
ans = 1
arr = []
print(2)
sample = int(input())
arr.append(sample)
for i in range(1, n):
    arr.append(int(input()))
    if arr[i] >= sample:
        ans += 1
        sample = arr[i]
# print(arr)
print(ans)