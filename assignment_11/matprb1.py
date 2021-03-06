def check_diagonal(matrix):
    n = len(matrix)
    ans = True
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][j] != 0:
                    ans = False
                    break
        if not ans:
            break
    return ans


def check_triangular(matrix):
    ans = True
    left = True
    right = True
    n = len(matrix)
    # right triangle
    for i in range(n-1):
        for j in range(i+1, n):
            if matrix[i][j] != 0:
                right = False
                break
        if not right:
            break
    # left triangle
    for i in range(1, n):
        for j in range(i):
            if matrix[i][j] != 0:
                left = False
                break
        if not left:
            break

    ans = right or left
    return ans


def check_symmetric(matrix):
    ans = True
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                ans = False
                break
        if not ans:
            break
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    symmetric = check_symmetric(matrix)
    triangular = check_triangular(matrix)
    diagonal = check_diagonal(matrix)

    ans = 0
    if symmetric:
        ans+=1
    if triangular:
        ans+=2
    if diagonal:
        ans+=4
    print(ans)