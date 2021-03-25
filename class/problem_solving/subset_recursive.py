def subset(li, idx, output):
    '''
    li -> input list
    idx -> is used to point to current element
    output -> output string
    '''
    if idx == len(li):
        print(output)
        return
    
    subset(li, idx+1, output + str(li[idx]) + ', ')
    subset(li, idx+1, output)
    return

li = list(map(str, input().split()))
subset(li, 0, '')