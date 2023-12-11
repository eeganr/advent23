from aoclib import *
import os
import math

day = 10

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

start = inp.index('S')
start = (start // (inp.index('\n') + 1), start % (inp.index('\n') + 1))

inp = inp.split('\n')

#access indicators
F = [['-', '7', 'J'], [], [], ['|', 'L', 'J']]
Seven = [[], [], ['-', 'L', 'F'], ['|', 'L', 'J']]
L = [['-', '7', 'J'], ['|', 'F', '7'], [], []]
J = [[], ['|', 'F', '7'], ['-', 'L', 'F'], []]
Dash = [['-', '7', 'J'], [], ['-', 'L', 'F'], []]
Pipe = [[], ['|', 'F', '7'], [], ['|', 'L', 'J']]
Dot = [[], [], [], []]
key = {'F': F, '7': Seven, 'L': L, 'J': J, '-': Dash, '|': Pipe, '.': Dot}

starttype = "F"
# starttype = "L"

distances = {}

def checknew(pos, came_from:
for c in range(4):
    posvectors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    posvector = posvectors[c]
    pos = tuple(map(lambda i, j: i + j, start, posvector))
    if pos[0] < 0 or pos[0] >= len(inp) or pos[1] < 0 or pos[1] >= len(inp[0]):
        continue
    if inp[pos[0]][pos[1]] in 
    if ok:
        print(list(key.keys())[list(key.values()).index(i)])
        break