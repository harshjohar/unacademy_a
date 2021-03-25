# cook your dish here
import sys
 
def n_mod_x(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    return int(input())
 
 
# ------------------------------------Do not touch anything above this line! -----------------------------------------
 
# The following function always returns 2, you should complete it so that it returns the hidden value always
# You can call n_mod_x upto 150 times
def guess():
    return n_mod_x(2*10**18)
 
# ------------------------------------Do not touch anything below this line! -----------------------------------------
 
T = int(input())
while T > 0:
    print('2 ' + str(guess()))
    x = int(input())
    # assert(x == 1)
    T-= 1