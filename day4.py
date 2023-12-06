from aoclib import *
import os

day = 4

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n')

inp = [[j.strip().split(' ') for j in i.split(':')[1].split('|')] for i in inp]


for i in range(len(inp)):
    while '' in inp[i][0]:
        inp[i][0].remove('')
    while '' in inp[i][1]:
        inp[i][1].remove('')

inp = [[[int(k) for k in j] for j in i] for i in inp]

sums = []

for sub in inp:
    sums.append(len(list(set(sub[0]).intersection(sub[1]))))

points = 0

for i in sums:
    if i > 0:
        points += 2**(i-1)

print(points)

cards = [1] * len(sums)

for i in range(len(sums)):
    for j in range(i+1, i+sums[i]+1):
        try:
            cards[j] += cards[i]
        except: pass

print(sum(cards))

