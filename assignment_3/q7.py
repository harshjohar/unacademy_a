n = int(input())
b = 0
mod = 0
i = 1
valid = True

while valid:
    mod = n%2
    n = n//2
    b = b + (i*mod)
    i *= 10

    if n < 1:
        valid = False

print(b)