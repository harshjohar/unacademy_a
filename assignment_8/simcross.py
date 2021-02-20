rows, columns = map(int, input().split())
maze = []
alphabet = list(map(chr, range(97, 123)))
for _ in range(rows):
    a = list(map(str, input()))
    maze.append(a)

# output = [list(map(str, '#'*columns))]*rows
output = maze[:]
# output = [['#' for _ in range(columns) for i in range(rows)]]
valid = True

w = int(input())
words = {}  # keys = length; values = word
for i in range(w):
    word = input()
    words[len(word)] = word

def c_length(maze, row, column):
    length = 0
    brackets = 0
    while brackets < 2 and row < len(maze):
        if maze[row][column] == '#':
            break
        elif maze[row][column] == 'c' or maze[row][column] == 'b':
            brackets += 1
            length += 1
        else:
            length+=1
        row += 1
    return length

def r_length(maze, row, column):
    length = 0
    brackets = 0
    while brackets < 2 and row < len(maze[0]):
        if maze[row][column] == '#':
            break
        elif maze[row][column] == 'r' or maze[row][column] == 'b':
            brackets += 1
            length += 1
        else:
            length+=1
        column += 1
    return length

def b_length(maze, row, column):
    tmp = column    # for reuse
    length_horizantal = 0
    length_vertical = 0
    brackets_h = 0
    brackets_v = 0

    # horizontal
    while brackets_h < 2 and row < len(maze[0]):
        if maze[row][column] == '#':
            break
        elif maze[row][column] == 'r' or maze[row][column] == 'b':
            brackets_h += 1
            length_horizantal += 1
        else:
            length_horizantal += 1
        column += 1
    
    # vertical
    while brackets_v < 2 and row < len(maze):
        if maze[row][tmp] == '#':
            break
        elif maze[row][tmp] == 'c' or maze[row][tmp] == 'b':
            brackets_v += 1
            length_vertical += 1
        else:
            length_vertical += 1
        row += 1

    return length_horizantal, length_vertical

# driver code
for i in range(rows):
    for j in range(columns):
        if valid:
            # BOTH
            if maze[i][j] == 'b':
                h, v = b_length(maze, i, j)
                for x in words:
                    if x == h:
                        req_word = words[x]
                req_list = list(map(str, req_word))
                for o in range(j, j+h):             
                    output[i][o] = req_list[o-j]
                    

                for x in words:
                    if x == v:
                        req_word = words[x]
                req_list = list(map(str, req_word))
                for o in range(i, i+v):                   
                    output[o][j] = req_list[o-i]
                    


            # VERTICAL
            elif maze[i][j] == 'c':
                # print(i, j)
                c = c_length(maze, i, j)
                # print(words[4])
                for x in words:
                    if x == c:
                        req_word = words[x]
                        print(words[x])
                req_list = list(map(str, req_word))
                # print(req_list)
                for o in range(i, i+c):
                    output[o][j] = req_list[o-i]
                    

            # HORIZONTAL
            elif maze[i][j] == 'r':
                r = r_length(maze, i, j)
                for x in words:
                    if x == r:
                        req_word = words[x]
                req_list = list(map(str, req_word))
                # print(req_list)
                for o in range(j, j+r):                 
                    output[i][o] = req_list[o-j]
                    
# print(words)

if valid:
    for i in range(rows):
        for j in range(columns):
            print(output[i][j], end='')
        print()
else:
    print('Invalid')

'''
LEFT:
Invalid
FUCK! bug in c......
'''