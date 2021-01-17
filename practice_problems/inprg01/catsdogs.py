t = int(input())

for test in range(t):
    c, d, l = [int(i) for i in input().split()]
    
    if c <= 2*d:
        if l <= 4*(c+d) and l >= 4*d and l%4 == 0:
            print('yes')
        else:
            print('no')
    elif c > 2*d:
        if l <= 4*(c+d) and l >= 4*(d+(c-2*d)) and l%4 == 0:
            print('yes')
        else:
            print('no')
        