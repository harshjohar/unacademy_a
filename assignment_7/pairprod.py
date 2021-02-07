print(2)
n = int(input())
arr = []
square = 0
for i in range(n):
    x = int(input())
    arr.append(x)
    square += x**2
s = sum(arr)
print(int(((s**2)-square)/2))