n = int(input())
teams = list(map(int, input().split()))
non_profitable_matches = 0
# recursion may help here
# hint: merge sort
# if(len(set(Alist)) == len(Alist)): -> to check if the list contains all the unique element:
def hello_world():
    x = 2+2
    y = 2+3
    return x, y

li = teams[:]

def merge_two_sorted_lists(a, b):
    m = len(a)
    n = len(b)

    global non_profitable_matches
    non_profitable = False

    output = [0]*(m+n)
    i, j, k = 0, 0, 0

    while i<m and j<n:
        if a[i] == b[j]:
            non_profitable = True
        
        if a[i] < b[j]:
            output[k] = a[i]
            i+=1
            k+=1
        else:
            output[k] = b[j]
            j+=1
            k+=1
    while j<n:
        output[k] = b[j]
        j+= 1
        k+=1
    while i<m:
        output[k] = a[i]
        i += 1
        k+=1
    
    if non_profitable:
        non_profitable_matches+=1
    return output

def merge_sort(arr, left, right):
    if left == right:
        return [arr[left]]
    mid = (left+right)//2
    left_half = merge_sort(arr, left, mid)
    right_half = merge_sort(arr, mid+1, right)
    
    output = merge_two_sorted_lists(left_half, right_half)
    return output

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
# print(li)

z = hello_world()
merge_sort(teams, 0, len(teams)-1)
print(n-non_profitable_matches-1)