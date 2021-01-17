from math import sqrt

t = int(input())
output = []

for i in range(t):
    n, v1, v2 = [int(i) for i in input().split()]

    time_lift = (2*n)/v2
    time_stairs = (sqrt(2)*n)/v1

    if time_lift < time_stairs:
        output.append('Elevator')
    else:
        output.append('Stairs')

for i in range(t):
    print(output[i])