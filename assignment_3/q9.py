n = int(input())

gcd = 1

a = int(input())
b = int(input())

if n ==2:
    for i in range(1, max(a, b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
else:
    for i in range(1, max(a, b)+1):
        if a%i == 0 and b%i == 0:
            gcd_o = i

    for k in range(1, n-1):
        c = int(input())
        for j in range(1, max(gcd_o, c)+1):
            if c%j == 0 and gcd_o%j == 0:
                gcd = j

print('gcd is: '+ str(gcd))