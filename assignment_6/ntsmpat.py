n = int(input())

for i in range(1, n+1):
    num = i
    # increasing
    for j in range(1, i+1):
        print(num, end=" ")
        num+=1
    # decreasing
    for k in range(i+1, 2*i):
        print(num-2, end=" ")
        num-=1
    print()