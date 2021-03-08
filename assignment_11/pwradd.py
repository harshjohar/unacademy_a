import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------
 
# The return value of this function is wrong, write the correct version of this function using the add(a, b) ...
# function defined above.
 
# Note that this function should return (a ** b) % m, you are guaranteed that add(a, b) returns (a + b) % m
 
def mul(a, b):
    res = 0
    for _ in range(0, b):
        res = add(res, a)
    return res
 

import random

def partition(li, left, right):
    # You are given a list of size N, ans an element from the list called as'pivot element'.
    # You need to segeregate all the elements lesser than pivot on the left side & greater than pivot on the right side in any order.    m = left
    m = left
    pivot_index = random.randrange(left, right)
    pivot = li[pivot_index]
    li[right], li[pivot_index] = li[pivot_index], li[right]
    for i in range(left, right):
        if li[i] <= pivot:
            li[i], li[m] = li[m], li[i]
            m+=1
    li[right], li[m] = li[m], li[right]
    return m

def quick_sort(li, left, right):
    if left>=right:
        return
    pivot_index = partition(li, left, right)
    quick_sort(li, left, pivot_index-1)
    quick_sort(li, pivot_index+1, right)

    return
li = [2, 3, 4, 1, 4, 6, 3, 9, -1, -7, 10]
quick_sort(li, 0, len(li)-1)


def median(a, b):
    if len(a) > len(b):
        return median(b, a)
    x = len(a)
    y = len(b)
    low = 0
    high = x
    while low <= high:
        partition_x = (low+high)//2
        partition_y = (x+y+1)//2 - partition_x

        if partition_x == 0:
            maxleft_x = -1*sys.maxsize
        else:
            maxleft_x = a[partition_x - 1]
        
        if partition_y == 0:
            maxleft_y = -1 * sys.maxsize
        else:
            maxleft_y = b[partition_y-1]

        if partition_x == x:
            minright_x = sys.maxsize
        else:
            minright_x = a[partition_x]

        if partition_y == y:
            minright_y = sys.maxsize
        else:
            minright_y = b[partition_y]
        
        if maxleft_x <= minright_y and maxleft_y <= minright_x:
            #found median
            if (x+y)%2 == 0:
                return (max(maxleft_x, maxleft_y) + min(minright_x, minright_y))
            else:
                return max(maxleft_x, maxleft_y)

        elif maxleft_x > minright_y:
            high = partition_x - 1
        else:
            low = partition_x+1
    return -1

x = [1, 2, 3, 4, 6, 8, 70]
y = [5, 77, 88, 90]
harsh = median(x, y)

def pwr(a, b):
    res = 1
    for _ in range(0, b):
        res = mul(res, a)
    return res
# --------------------- Do not touch anything below this line ----------------------
 
a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)