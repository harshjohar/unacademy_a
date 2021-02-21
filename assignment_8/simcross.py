# input
rows, columns = map(int, input().split())
maze = []


row_dict, column_dict = {}, {}

for r in range(rows):
    row = list(input())
    maze.append(row)
    tmp = []    # for calculating the lenght of horizontal word
    for i in range(columns):
        letter = row[i]
        if letter == 'r' or letter == 'b':
            tmp.append(i)
    if len(tmp) != 0:
        row_dict[tmp[1]-tmp[0]+1] = [r, tmp[0]]     # coordinates of the initial letter is the value and the length is key

for c in range(columns):
    tmp = []
    for i in range(columns):
        row = maze[i]
        letter = row[c]
        if letter == 'c' or letter == 'b':
            tmp.append(i)
        if len(tmp) != 0:
            column_dict[tmp[1]-tmp[0]+1] = [tmp[0], c]      # coordinates of the initial letter is the value and the length is key

words_dict = {}
w = int(input())
for _ in range(w):
    w = input()
    words_dict[len(w)] = w

# processing
maze = [['#']*rows for i in range(columns)]


length_d = set(row_dict.keys()) | set(column_dict.keys())
if length_d != set(words_dict.keys()):
    print('Invalid')
    exit()

for length in row_dict.keys():
    rc = row_dict[length]
    c = rc[1]
    row = maze[rc[0]]
    word = words_dict[length]

    i = 0
    for index in range(c, c+length):
        row[index] = word[i]
        i+=1

for length in column_dict.keys():
    rc = column_dict[length]
    r = rc[0]
    row = maze[rc[0]]
    c = rc[1]
    word = words_dict[length]
    i = 0
    for j in range(r, r+length):
        row = maze[j]
        letter = row[c]
        if letter != '#':
            if letter != word[i]:
                print('Invalid')
                exit()
        row[c] = word[i]
        i+=1

# output
for i in range(rows):
    for j in range(columns):
        print(maze[i][j], end='')
    print()