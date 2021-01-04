h = int(input())

for i in range(h):
    for space in range(h - i, 1, -1):
        print(' ', end='')
    for hash in range(i+1):
        print('# ', end = '')
    print()

for j in range(h):
    for spaceb in range(j+1):
        print(' ', end = '')
    for hashb in range(h - j, 1, -1):
        print('# ', end = '')
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