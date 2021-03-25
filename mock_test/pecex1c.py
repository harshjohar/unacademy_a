# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = set(a)
    b = set(b)
    
    c = a.intersection(b)
    print(len(c))