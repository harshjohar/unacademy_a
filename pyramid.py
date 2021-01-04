h = int(input())

for i in range(h):
    for space in range(h - i, 1, -1):
        print(' ', end='')
    for hash in range(i+1):
        print('#', end = '')
    for rhash in range(i):
        print('#', end = '')
    print()