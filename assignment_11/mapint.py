n = int(input())
database = {}
frequency_map = {}
potential_ans = []
count = 0
for _ in range(n):
    a,b,c,d = input().split()
    # a, b = endpoints
    # c = street name
    # d = direction (no use)

    a = int(a)
    b = int(b)
    if a in frequency_map:
        frequency_map[a] += 1
    else:
        frequency_map[a]=1
    if b in frequency_map:
        frequency_map[b]+=1
    else:
        frequency_map[b]=1

    if a in database:
        database[a].append(c)
    else:
        database[a] = [c]
    if b in database:
        database[b].append(c)
    else:
        database[b] = [c]
    
for i in frequency_map:
    if frequency_map[i] == 4:
        potential_ans.append(i)

for i in potential_ans:
    s = set(database[i])
    if len(s) == 2:
        count+=1



# print(frequency_map)
# print(database)
# print(potential_ans)
print(count)