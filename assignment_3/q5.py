n = int(input())
p = 1
count = 0
valid = True

while valid:
    if p <= n:
        print(p, end = ', ')
        p *= 2
        count += 1
    else:
        valid = False

print('\n' + str(count))

# answer for given question : 20