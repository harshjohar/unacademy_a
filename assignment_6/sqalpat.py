n = int(input())
num = 1
for i in range(1, n+1):
    if i%2 == 1:
        for j in range(5):
            print(num, end=' ')
            num+=1
    else:
        for k in range(5):
            print(num+4, end=' ')
            num-=1
        num+=10
    print()