# new data type -- None
# used to give the notion of empty quantiy
none = None
print(none)
print(type(none))

"""Tuples"""
# tuples are collection of heterogeneous objects
# tuples are immutable
# initialised by : <name> = ()

x = (1, 2,3 ,34, 4, 55, 5, 6, 6, 'harsh', 'hi')
print(x)

# tuples are immutable

# access any element
# same as list___ zero based indexing
print(x[2], x[6])

""" 
Differences from lists
--> cannot update the elements in tuple
--> elements cannot be deleted
"""

# OPERATIONS
print(x*4)
print(3 in x)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2) # concatination works!

# slicing op
print(x[1:4])
print(x[::-1])

# use of tuple
def test():
    # we want to return multiple values from the function
    return 1, 2, 3, 4, 'hi'

t = test()
print(t)
print(type(t))

"""dictionary"""
# stores data in format of -->  key: value
# we can store multiple values in this
# key should always be an immutable quantity
# like tuple, strings etc.
# doesn't store it sequentially, just randomly

d = {
    'name': 'harsh',
    'age': '18',
    'college': 'pec'
}
print(d)
print(d['name'])

# dictionaries are mutable
d['name'] = 'harshpreet'
print(d)

# how to add a key, value pair
d['location'] = 'banga'
print(d)

# delete
del d['location']
print(d)

# puthia hrkta
# print(d['qwerty']) # error
print(d.get('qwerty'), d.get("college"))

# if you want to delete everything
# --> d.clear()

# print all he keys
keys = d.keys()
print(keys)
# print all values
values = d.values()
print(values)

"""SETS"""
# sets are same as dictionaries with just a differnec thatt it has only keys, and no values in it.
# sets are mutable

s = {'harsh', '18', 'banga'}
print(s)
print(type(s))