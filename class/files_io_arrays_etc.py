# module = pre-defined python files
import math

fact = math.factorial(60)
print(fact)

log_10 = math.log10(100000000)
print(log_10)

"""arrays"""
# homogenous list(simple definition)
import array

"""
types:
i -> integer
d -> double
f -> float
"""
arr = array.array('i', [1, 2, 3, 4])
print(arr)
arr.append(34)
arr.insert(0, 675)
for i in arr:
    print(i)


"""PYC wala condept"""
# python -m compileall

"""File I/O"""
# open function
'''
'r' = read only mode
'r+' = opens for reading and writing both
'w' = write only, if the fil exsist, then it will overwrite everything; else, create a new file
'w+' = read/write both
'a' = append the data, otherwise new file
'rb' = read in binary --> helpful in reading complex files like images etc.
'+' = every + will activate all modes
'''
f = open('input.txt', 'r')
r = f.read() # expects the number of bytes to count
print(r)
print(f.tell()) # gives the position of cursor

# relocating the cursor
f.seek(0) # brings the cursor at th epassed argument
print(f.tell())

print(f.readline()) # read the full line until'\n' character

# write
f = open('output.txt', 'w')
f.write('harsh')

# append
f = open('input.txt', 'a')
f.write('ghch fsb gu\n')

# write binary
f = open('binary.txt', 'ab')
# f.write('harsh') --> give error
f.write(b'0x123\n')

# closing file is necessary
f.close() # saving memory, and avoid error