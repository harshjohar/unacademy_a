def subsets(ls):

    ans = [[]]

    for i in range(len(ls)):
        tmp = [ans[j][:] for j in range(len(ans))]
        n = ls[i]

        for j in range(len(ans)):
            tmp[j].append(n)
        ans = ans+tmp
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    inp = []
    for i in range(1, n+1):
        inp.append(i)
    
    out = subsets(inp)

    for i in range(len(out)):
        for j in range(len(out[i])):
            print(out[i][j], end=' ')
        print()