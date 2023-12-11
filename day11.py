from aoclib import *
import os
import math

day = 11

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n')

rows2add = []
cols2add = []

for i in range(len(inp)):
    empty = True
    for j in range(len(inp[i])):
        if inp[i][j] == '#':
            empty = False
            break
    if empty:
        rows2add.append(i)

for col in range(len(inp[0])):
    empty = True
    for j in range(len(inp)):
        if inp[j][col] == '#':
            empty = False
            break
    if empty:
        cols2add.append(col)


pos = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == '#':
            pos.append((i, j))

distances = []

for i in range(len(pos)):
    for j in range(len(pos)):
        if j >= i: break
        a, b = (pos[j][0], pos[i][0]) if pos[i][0] > pos[j][0] else (pos[i][0], pos[j][0])
        c, d = (pos[j][1], pos[i][1]) if pos[i][1] > pos[j][1] else (pos[i][1], pos[j][1])
        distances.append(b - a + sum([int(1e6-1) if m > a and m < b else 0 for m in rows2add]) + d - c + sum([int(1e6-1) if m > c and m < d else 0 for m in cols2add]))
        
print(sum(distances))