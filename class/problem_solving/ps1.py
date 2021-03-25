# print all natural numbers till n <by recursion>
def natural_recursive(n):
    if n==1:
        print(1)
        return
    # recursive assumption
    natural_recursive(n-1)
    print(n)
    return

# print all natural numbers till n in decreasing order < by recursion >
def ulta_rec(n):
    if n == 1:
        print(1)
        return
    print(n) 
    ulta_rec(n-1)
    return

# given a list of integers, write a function to check if the list is arranged in increasing order <by recursion>
def list_check(arr, i):
    if i == len(arr) - 1:
        return True
    isSorted = list_check(arr, i+1)
    if isSorted==True:
        return arr[i] <= arr[i+1]
    else:
        return False

# stairs
# from any step you can either jump by one step or two step
# in how many different ways you can reach the last step
# print all the valid patterns

def stairs(n, i, path):
    # i = current position
    # path = string -> stores the current path
    if i>n:
        return
    if i==n:
        print(path)
        return
    
    stairs(n, i+1, '1 '+path)
    stairs(n, i+2, '2 '+path)



n = int(input())
arr = list(map(int, input().split()))


natural_recursive(n)
print('______')
ulta_rec(n)
print('______')
li_chk=list_check(arr, 0)
print(li_chk)
print('______')
stairs(n, 0, '')
