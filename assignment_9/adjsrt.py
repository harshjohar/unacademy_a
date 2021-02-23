n = int(input())
li = list(map(int, input().split()))

# maybe bubble sort
def adjacent_sort(li):
    ans = []
    for j in range(len(li)):
        swap = False
        for i in range(len(li)-j-1):    # did this because the comparison with last elemnt is not required
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                ans.append(i)
                swap = True
        if not swap:
            return ans # if no swap in whole iteration menas the list is sorted
    return ans

ans = adjacent_sort(li)
print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=' ')