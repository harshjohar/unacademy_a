N = int(input())
arr = []

for i in range(N):
    p = int(input())
    arr.append(p)

b = True

for j in range(N//2):
    if arr[j] == arr[N-j-1]:
        continue
    else:
        b = False
        break

if b == True:
    print("Yes")
else:
    print("No")