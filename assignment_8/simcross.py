rows, columns = map(int, input().split())

maze = []
for _ in range(rows):
    maze.append(list(map(str, input())))

# output = deepcopy(maze)
# output is a maze of only {#} of same size as the original maze
output = [['#']*rows for i in range(columns)]

words_dict = {}
w = int(input())
for _ in range(w):
    w = input()
    words_dict[len(w)] = w

def vertical_c(maze, row, column):
    # returns the length of word starting with c and eding with b/c
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

def horizontal_r(maze, row, column):
    # returns the length of word starting with r and eding with b/r
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

def both_b(maze, row, column):
    # returns the length of word(vertical) starting with b and eding with b/c and length of word(horizontal) starting with b and ending with b/r
    length_horizontal, length_vertical = 0, 0
    tmp = column    # for reuse
    brackets_h = 0
    brackets_v = 0
    while brackets_h < 2 and row < len(maze[0]):
        if maze[row][column] == '#':
            break
        elif maze[row][column] == 'r' or maze[row][column] == 'b':
            brackets_h += 1
            length_horizontal += 1
        else:
            length_horizontal += 1
        column += 1

    while brackets_v < 2 and row < len(maze):
        if maze[row][tmp] == '#':
            break
        elif maze[row][tmp] == 'c' or maze[row][tmp] == 'b':
            brackets_v += 1
            length_vertical += 1
        else:
            length_vertical += 1
        row += 1
    return length_horizontal, length_vertical

for i in range(rows):
    for j in range(columns):

        # BOTH
        if maze[i][j] == 'b':
            b_horizontal, b_vertical = both_b(maze, i, j)
            
            # vertical
            req_word = words_dict[b_horizontal]
            if b_horizontal != 1:
                for o in range(i, i+b_horizontal):
                    if output[i][j] != '#':
                        if req_word[o-i] != output[o][j]:
                            print('Invalid')
                            exit()
                    output[o][j] = req_word[o-i]
            
            # horizontal
            req_word = words_dict[b_vertical]
            if b_vertical != 1:
                for o in range(j, j+b_vertical):
                    if output[i][j] != '#':
                        if req_word[o-j] != output[i][o]:
                            print('Invalid')
                            exit()
                    output[i][o] = req_word[o-j]

        # VERTICAL
        if maze[i][j] == 'c':
            c_length = vertical_c(maze, i, j)
            req_word = words_dict[c_length]
            if c_length != 1:
                for o in range(i, i + c_length):
                    if output[o][j] != '#':
                        if req_word[o-i] != output[o][j]:
                            print('Invalid')
                            exit()
                    output[o][j] = req_word[o-i]

        # HORIZONTAL
        if maze[i][j] == 'r':
            r_length = horizontal_r(maze, i, j)
            req_word = words_dict[r_length]
            if r_length != 1:
                for o in range(j, j+r_length):
                    if output[i][o] != '#':
                        if req_word[o-i] != output[i][o]:
                            print('Invalid')
                            exit()
                    output[i][o] = req_word[o-j]

for i in range(rows):
    for j in range(columns):
        print(output[i][j], end='')
    print()