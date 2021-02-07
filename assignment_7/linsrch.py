print(1)
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = set(arr)

q = int(input())
for i in range(q):
    s = int(input())
    if s in arr:
        print('yes')
    else:
        print('no')