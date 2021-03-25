""" Q1 """

# You are given an integer list of size n. (n<= 10^7). 
# Now, after taking input of the list you will get another integer q. (q<=10^5).
# q represents number of queries.
# you will get q queries and inside each query you ll get two numbers denoting index of list l and r. (0 <= l, r <= n-1) 
# you have to print sum of elements from l to r, for each query.

#python basic
def query_inbuilt(li, l, r):
    li = li[l:r+1]
    return sum(li)

# brute force
def query_basic(li, l, r):
    sum = 0
    for i in range(l, r+1):
        sum += li[i]
    return sum

# fully optimised
def cumulative(li):
    li_o = [li[0]]
    for i in range(1, len(li)):
        li_o.append(li[i]+li_o[i-1])
    return li_o

def query_adv(li, l, r):
    li_o = cumulative(li)
    if l != 0:
        return li_o[r] - li_o[l-1]
    else:
        return li_o[r]

li = list(map(int, input('li: ').split()))
# print(cumulative(li))
q = int(input('q: '))
for _ in range(q):
    l, r = map(int, input('l, r: ').split())
    print(query_inbuilt(li, l, r), query_basic(li, l ,r), query_adv(li, l, r))


""" Q2 """
# given a list of integers of size n. print all the subsets of the given list. <recursion>, n<=20.
# reason behind 2^n number of subsets. Every element has two choices whetehe to get included or not.
def subset(li, idx, output):
    '''
    li -> input list
    idx -> is used to point to current element
    output -> output string
    '''
    if idx == len(li):
        print(output)
        return
    
    subset(li, idx+1, output + str(li[idx]) + ', ')
    subset(li, idx+1, output)
    return

li = [1, 2, 3]
print(subset(li, 0, ''))

''' Q3 '''
# iteratively getting subsets
def subset_iterative(li):
    num = 2**len(li)
    for i in range(num):
        pass             
