# cook your dish here
for _ in range(int(input())):
    n = int(input())
    iterations = int(n**0.5)
    i = 1
    li = []
    while i <= n:
        li.append(i**2)
        i+=1
    # print(li)
    ans = []
    for i in range(iterations):
        b = n - li[i]
        if b in li:
            ans.append((int(min(li[i]**0.5, b**0.5)), int(max(li[i]**0.5, b**0.5))))
    ans = list(set(ans))
    ans.sort(key=lambda x:x[1])
    if len(ans)<2:
        print('-1 -1 -1 -1')
    else:
        print(ans[0][0], ans[0][1], ans[1][0], ans[1][1])