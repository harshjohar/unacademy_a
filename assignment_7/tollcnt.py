import math

n = int(input())
data = {}
collection = 0
for _ in range(n):
    action = input()
    if action == 'entry':
        license_number = input()
        data[license_number] = int(input())
    elif action == 'exit':
        license_number = input()
        time = int(input())
        elapsed = time - data[license_number]
        # print('e', elapsed)
        payable = elapsed/60
        
        payable = math.ceil(elapsed/60) - 1 # first hour is mandatory
        # print('p', payable)
        if payable >= 0:
            collection += (60 + 30*payable) 
    
print(collection)