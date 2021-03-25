# find special elemnt in the given list (which appers only once)
# n <= 1e6
''' use xor '''
def unique(li):
    x=0
    for i in range(len(li)):
        x = x^li[i]
    return x
given = list(map(int, input().split()))
print('unique', unique(given))

# xor sums # trulove.guru/watch.php?ref=RQHM6E.mp4

def unique_dict(string):
    dict = {}
    for i in range(len(string)):
        if dict.get(string[i]) == None:
            dict[string[i]] = 1
        else:
            dict[string[i]] += 1

    result = []
    for i in dict.keys():
        if dict[i] == 1:
            result.append(i)
    return result
string = input()
print(unique_dict(string))