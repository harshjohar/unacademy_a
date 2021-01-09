b = True
arr = []

while b:
    n = int(input())
    if n == 0:
        b = False
    else:
        arr.append(n)

if b == False:
    for j in range(len(arr)):
        print(arr[n-j-1], end=', ')