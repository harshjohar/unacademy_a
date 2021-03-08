import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------
 
# A sample function that computes (2 * a) % m using add(a, b)
def twice(a):
    return add(a, a)
 
def pwr(a, b):
    return 0
 
# --------------------- Do not touch anything below this line ----------------------
 
 
a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)