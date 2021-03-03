import sys
import random
 
limit = 0
count = 0
 
def run_program(m):
    global count
    count = count + 1
    if count > 31:
        print("Took more than 31 queries for limit = " + str(limit))
        exit()
    if m <= limit:
        return True
    else:
        return False
 
 
# ------------------- Do not touch anything above this line -------------------------------------
 
# copy your solution here
def find_memory_limit():
    lo = 1
    hi = 1000000000-1

    while lo <= hi:
        mid = (lo+hi)//2
        # length = hi-lo+1
        if run_program(mid):
            lo = mid+1
        
        else:
            hi = mid-1
        
    return hi
 
# ------------------- Do not touch anything below this line -------------------------------------
 
for _ in range(0, 1000):
    limit = random.randint(1, 999999999)
    count = 0
    found = find_memory_limit()
    if found != limit:
        print('Error found limit = ' + str(found) + ', when actual limit = ' + str(limit))
        exit()
 
print('your program passed 1000 random testcases!')