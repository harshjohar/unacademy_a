d = int(input())
arr = []

for i in range(d):
    c = int(input())
    if c == 0:
        c = 1
    arr.append(c)

count = 0

for j in range(d-1):
    if arr[j] * arr[j+1] < 0:
        count += 1

output = []

if count >= 2:
    while count >= 0:
        output.append(count)
        count -= 2
    for i in range(len(output)):
        print(output[len(output) - i - 1], end=' ')
    print('')
else:
    print(count)