n = int(input())
A = []
B = []
C = []

for i in range(n):
    x = int(input())
    A.append(x)

for j in range(n):
    y = int(input())
    B.append(y)

for k in range(n):
    z = A[k] + B[k]
    C.append(z)

for l in range(n):
    print(C[l])