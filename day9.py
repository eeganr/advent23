from aoclib import *
import os
import math

day = 9

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n')

inp = [i.split() for i in inp]

inp = [[int(j) for j in i] for i in inp]

total = 0

for history in inp:
    subsequents = [history.copy()]
    while True:
        temp = []
        for i in range(len(subsequents[-1])-1):
            temp.append(subsequents[-1][i+1] - subsequents[-1][i])
        subsequents.append(temp)
        if temp == [0]*len(temp):
            break
    
    for i in reversed(range(len(subsequents))):
        if i == len(subsequents) - 1:
            subsequents[i].append(0)
            continue
        subsequents[i].append(subsequents[i+1][-1] + subsequents[i][-1])
    
    total += subsequents[0][-1]

print(total)

total = 0


for history in inp:
    subsequents = [history.copy()]
    while True:
        temp = []
        for i in range(len(subsequents[-1])-1):
            temp.append(subsequents[-1][i+1] - subsequents[-1][i])
        subsequents.append(temp)
        if temp == [0]*len(temp):
            break
    
    for i in reversed(range(len(subsequents))):
        if i == len(subsequents) - 1:
            subsequents[i] = [0] + subsequents[i]
            continue
        subsequents[i] = [subsequents[i][0] - subsequents[i+1][0]] + subsequents[i]
    
    total += subsequents[0][0]

print(total)