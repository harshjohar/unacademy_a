# cook your dish here
count = 0

def solve(n, x):
    global total_stairs
    global count
    if x == 0:
        if n==0:
            count+=1
        else:
            return
            
    else:
        if n>0:
            solve(n-1, x-1)
        if n>1:
            solve(n-2, x-1)
        if n>2:
            solve(n-3, x-1)
        if n<total_stairs:
            solve(n+1, x-1)
        if n<total_stairs-1:
            solve(n+2, x-1)
        if n<total_stairs-2:
            solve(n+3, x-1)
        solve(n, x-1)
            

for _ in range(int(input())):
    n,x = map(int, input().split())
    count = 0
    total_stairs=n
    solve(n, x)
    print(count)
    