h = int(input())

j = 1
a = h//2 + 1

while j <= a:
    t = 1
    while t <= a - j:
        print(' ', end='')
        t += 1

    i = 1
    while i <= j:
        print('*', end=' ')
        i += 1
    
    j += 1
    print()

j = a - 1

while j != 0:
    t = 1
    while t <= a - j:
        print(' ', end='')
        t += 1

    i = 1
    while i <= j:
        print('*', end=' ')
        i += 1
    
    j -= 1
    print()






# for h = 9
'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''