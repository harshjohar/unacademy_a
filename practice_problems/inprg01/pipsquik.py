t = int(input())

output = []

for i in range(t):
    n, h, y1, y2, l = [int(i) for i in input().split()]
    number = 0
    barrier = []
    for i in range(n):
        barrier.append([int(i) for i in input().split()])
    
    for i in range(n):
        if barrier[i][0] == 1:                  #type 1 barrier
            if (h - y1) <= barrier[i][1]:
                number += 1
            else:
                if l > 1:
                    number += 1
                    l -= 1
                else:
                    break
                
        elif barrier[i][0] == 2:                #type 2 barrier
            if y2 >= barrier[i][1]:
                number += 1
            else:
                if l > 1:
                    number += 1
                    l -= 1
                else:
                    break
    output.append(number)

for i in range(t):
    print(output[i])