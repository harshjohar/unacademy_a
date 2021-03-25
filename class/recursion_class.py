def swap(a, b):
    print('initial: ', a, b)
    tmp = a
    a = b
    b = tmp
    print('after: ', a, b)

def python_op(a, b):
    a, b = b, a
    print('python op: ', a, b)
a=8
b=43
swap(a, b)
python_op(a, b)
print('OG: ', a, b) # global varirables

# pass by value and reference
def update_list(li):
    print('before: ', li)
    li.append(10)
    print('after: ', li)

li = [1,2,3,4,5,5]
print('OG: ', li)
update_list(li)
print('update_try: ', li)

def str_update(string):
    print('string in: ', string)
    string += 'abc'
    print('string out: ' , string)

string = 'hello '
print('OG: ', string)
str_update(string)
print('without_f: ', string)

# list is effected by functions but strings are not
# when lists are passed, they are passed by REFERENCE: so all changes persists
# in case of "int, str, bool, float" : they are passed by VALUE i.e. a copy is passed:
# so the changes do not persist outside the function

""" RECURSION """
# y = f(x)
# y' = g(x)
# y" = f(g(x))
# ....
"""
    y=f(x)
    f(f(x'))    x = f(x')
    f(f(f(x"))) x' = f(x")
"""
# Mathematically, recursion is the process where we have speacil composite function, where the compostion is made such that function calls itself, inside it only; with/without the same parameter.

# In programming, recursion is defined as a tool, where a function solving a bigger problem, calls itself inside it to solve another problem till the time we reach to a stage where we have the smallest already solved problem with an extra memory buffer.

# PMI
# check for n=1(SMALLEST POSSIBLE PROBLEM)
# assume true for n=k
# P/T: true for n=k+1

# recursion steps
# 1. base case
# 2. assumption
# 3. self work

def factorial(n):
    if n == 1:              # base case
        return n

    value = factorial(n-1) # assumption
    ans = n*value          # self work
    return ans

print(factorial(8))

def fact_mini(n):
    if n==1 or n==0:
        return 1
    return n*fact_mini(n-1)

print(fact_mini(7))

def fibonacci(n):
    if n==1 or n==0:
        return n
    
    ans = fibonacci(n-1) + fibonacci(n-2)
    return ans

print(fibonacci(10))

# memory has 2 parts(major)
# (a) call stack
# stack = add on top and remove from top
# whenever a function is called, then we add an entry to the top of stack. This entry is called stack frame.
# What is in the frame?
# -> All the local variables are stored here
# return -> removes the entry from the frame in the call stack.  


"""
loops are space optimised, recursion is not
BUT
some algorithms are really easy to implement via recursion.
"""
# (b) heap(pool) --> bhool jao