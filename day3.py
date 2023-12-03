from aoclib import *
import os

day = 3

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n')

partsum = 0

tags = {}

for row in range(len(inp)):
    col = 0
    while col < (len(inp[row])):
        if inp[row][col].isdigit():
            num_len = 1

            temptags = []

            for i in range(col + 1, len(inp[row])):
                if inp[row][i].isdigit():
                    num_len += 1
                else:
                    break
            
            num = int(inp[row][col:col + num_len])

            for check_row in range(row - 1, row + 2):
                for check_col in range(col - 1, col + num_len + 1):
                    try:
                        if inp[check_row][check_col] != '.' and not inp[check_row][check_col].isdigit():
                            temptags.append(str(check_row) + '|' + str(check_col))
                    except:
                        pass

            # This simultaneously sets the flag
            if len(temptags) > 0:
                partsum += num
                for j in temptags:
                    if j not in tags: tags[j] = [num]
                    else: tags[j].append(num)

            col += num_len
        col += 1

print(partsum)

gearratiosum = 0
for i in tags.values():
    if len(i) == 2:
        gearratiosum += (i[0] * i[1])
print(gearratiosum)