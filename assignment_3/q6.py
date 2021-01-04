n = int(input())
x = 1

valid = True

while valid:
    if n % 2**(x+1) == 0:
        x += 1
    else:
        print(x)
        valid = False