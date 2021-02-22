# we need O(n) swaps so we will use 'selection sort'
def find_min(li, i):
    min = i
    i+=1
    while i<len(li):
        if li[i] < li[min]:
            min = i
        i+=1
    return min
def number_of_swaps(li):
    i=0
    swaps = []
    while i<len(li):
        min = find_min(li, i)
        if i != min:
            li[i], li[min] = li[min], li[i]
            swaps.append([i, min])
        i+=1
    return swaps

n = int(input())
arr = list(map(int, input().split()))
swaps = number_of_swaps(arr)
print(len(swaps))

for i in swaps:
    print(i[0], i[1])
    