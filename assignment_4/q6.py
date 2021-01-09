d = int(input())
arr = []

for i in range(d):
    c = int(input())
    arr.append(c)

x = int(input())

power = 0
result = 0

for p in range(d):
    r = arr[p] * (x**(power))
    power += 1
    result += r

print(result)