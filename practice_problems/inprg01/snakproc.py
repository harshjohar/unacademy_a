r = int(input())
output = []
def result(n):
    b = True
    for i in range(len(n)):
        if i%2 == 0 and n[i] == 'H':
            continue
        elif i%2 == 1 and n[i] == 'T':
            continue
        else:
            b = False
            break
    return b
        

for i in range(r):
    l = int(input())
    s = str(input())
    
    new = []
    head = 0
    tail = 0

    for i in range(l):
        if s[i] == 'H':
            new.append('H')
            head += 1
        elif s[i] == 'T':
            new.append('T')
            tail += 1
    
    if head != tail:
        output.append('Invalid')

    elif result(new) == False:
        output.append('Invalid')

    else:
        output.append('Valid')

for i in range(len(output)):
    print(output[i])