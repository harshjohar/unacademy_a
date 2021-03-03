import sys
import random
 
arr = []
queries_count = 0
def find_pos(x):
    global queries_count
    queries_count = queries_count + 1
    if queries_count > 40:
        print('error, took more than 40 queries')
        print('hidden array = ', arr, 'x = ', x)
        exit()
 
    if x < 0 or x >= len(arr):
        print('error, index out of range')
        print('hidden array = ', arr, 'x = ', x)
        exit()
    return arr[x]
    
# ----------------- Do not modify anything above this line -----------------------
# copy your solution here
def bisect_left(n, x):
    lo = 0
    hi = n

    while lo<hi:
        mid = (lo+hi)//2
        if find_pos(mid) < x:
            lo = mid+1
        else:
            hi = mid
    return lo

def bisect_right(n, x):
    lo = 0
    hi = n

    while lo<hi:
        mid = (lo+hi)//2
        if find_pos(mid) > x:
            hi = mid
        else:
            lo = mid+1
    return lo

def count(n, x):
    # n = size
    # x = target
    
    l = bisect_right(n, x) - bisect_left(n, x)

    return l
 
# ----------------- Do not modify anything below this line -----------------------
 
n = random.randint(1, 100000)
dict = {}
for _ in range(0, n):
    app = random.randint(0, 100000)
    arr.append(app)
    dict[app] = dict.get(app, 0) + 1
 
arr = sorted(arr)
 
for _ in range(1, 1000):
    queries_count = 0
    x = random.randint(0, 100000)
    ans = count(len(arr), x)
    if ans != dict.get(x, 0):
        print('Wrong answer, expected = ', dict.get(x, 0), 'got = ', ans)
        print('hidden array = ', arr, 'x = ', x)
        exit()
 
print('Correct Answer!')