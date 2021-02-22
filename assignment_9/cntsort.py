t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    for i in range(n):
        print(li[i], end=' ')
    print()