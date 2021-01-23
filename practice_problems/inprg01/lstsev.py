n = int(input())
u = n%10
t = (n%100-u)/10
if t==7:
    print(1)
else:
    print(0)