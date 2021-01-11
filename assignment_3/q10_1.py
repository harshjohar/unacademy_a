h = int(input())

for r in range(h+1):
    j = h
    while j > r:    #print spaces
        print(' ', end = '')
        j -= 1
    for q in range(r+1):
        k = 1
        for l in range(1, q+1):
            k *= l      # k = q!
        
        m = 1       # m is numerator in expansion of ncr
        for n in range(r, r - q, -1):
            m *= n

        c = m/k
        print(int(c), end='  ')

    print()