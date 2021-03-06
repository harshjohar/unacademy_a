t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    ans = ''
    N, E, W, S = 0, 0, 0, 0
    if x1 <= x2 and y1 <= y2:
        # bottom left to top right
        # N, E
        E = x2-x1
        N = y2-y1
    elif x1 <= x2 and y1 >= y2:
        # top left to bottom right
        # S, E
        E = x2-x1
        S = y1-y2
    elif x1 >= x2 and y1 <= y2:
        # bottom right to top left
        # N, W
        W = x1-x2
        N = y2-y1
    elif x1 >= x2 and y1 >= y2:
        # top right to bottom left
        # S, W
        W = x1-x2
        S = y1-y2
    else:
        # x1, y1 == x2, y2
        pass

    for i in range(N):
        ans+='N'
    for i in range(S):
        ans+='S'
    for i in range(E):
        ans+='E'
    for i in range(W):
        ans+='W'
    
    print(len(ans))
    print(ans)