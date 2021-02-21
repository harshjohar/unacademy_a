import copy
characters = {"a", 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
answer = list()
encryptions = list()
words_given = list()
mapping = dict()
n = int(input())
for i in range(n):
	words_given.append(input())
encryptions = list(map(str, input().split()))
copy_ = dict()

def decipher(i):
    if i == len(encryptions):
        answer.append(copy.deepcopy(mapping))      
        return     
    else:
        for j in range(len(words_given)):
            success = False
            ele_map = set()       
            if len(encryptions[i])==len(words_given[j]):
                success, ele_map = main_mapping(encryptions[i], words_given[j])
            if success:
                decipher(i+1)
            rem(encryptions[i], ele_map) 
        return

def main_mapping(string1, string2):
    ele_map = set()
    for j in range(len(string1)):
        if string1[j] in mapping.keys() and string1[j] in characters:
            if mapping[string1[j]] != string2[j]:
                return False, ele_map
        else:
            if string1[j] in characters:
                if string1[j] not in mapping.keys() and string2[j] not in mapping.values():
                    mapping[string1[j]] = string2[j]
                    ele_map.add(string1[j])
                else:
                    return False, ele_map
    return True, ele_map

def rem(string, ele_map):
    for j in range(len(string)):
        if string[j] in mapping and string[j] in ele_map:
            del mapping[string[j]]

decipher(0)
def solver(string):
    if string == 'i':
        return 'i'
    return answer[0][string]
for iter in range(len(encryptions)):
    for temporary in range(len(encryptions[iter])):
        print(solver(encryptions[iter][temporary]), end='')
    print(" ", end='')