from aoclib import *
import os
import re
from functools import reduce

day = 2

def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))

colors = ['blue', 'red', 'green']

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    # Read the input file and return a list of lines
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input('Puzzle2.txt')

inp = [[[k.strip() for k in j.split(',')] for j in i.split(';')] for i in [i.split(':')[1].strip() for i in inp.split('\n')]]

redcounts = []
greencounts = []
bluecounts = []
for p in inp:
    gamered = []
    gamegreen = []
    gameblue = []
    for i in p:
        bluecount = 0
        redcount = 0
        greencount = 0
        for j in i:
            if j[-3:] == 'red':
                redcount += int(j.split()[0])
            if j[-5:] == 'green':
                greencount += int(j.split()[0])
            if j[-4:] == 'blue':
                bluecount += int(j.split()[0])

        gamered.append(redcount)
        gamegreen.append(greencount)
        gameblue.append(bluecount)
    redcounts.append(gamered)
    greencounts.append(gamegreen)
    bluecounts.append(gameblue)

goodtrials = 0

maxcounts = [12, 13, 14]
for i in range(len(inp)):
    flag = True
    for j in range(len(inp[i])):
        if redcounts[i][j] > maxcounts[0] or greencounts[i][j] > maxcounts[1] or bluecounts[i][j] > maxcounts[2]:
            flag = False
            break
    if flag: goodtrials += i+1

maxblues = [max(i) for i in bluecounts]
maxreds = [max(i) for i in redcounts]
maxgreens = [max(i) for i in greencounts]

powers = [mb*mr*mg for mb,mr,mg in zip(maxblues, maxreds, maxgreens)]

print(goodtrials)
print(sum(powers))