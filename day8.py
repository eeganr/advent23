from aoclib import *
import os
import math

day = 8

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n')

directions = inp[0]

inp = inp[2:]

inp = [i.split(' = ') for i in inp]

dic = {}

for element in inp:
    dic[element[0]] = (element[1][1:4], element[1][6:9])


def search(seed):
    count = 0
    curr = seed
    while not curr == 'ZZZ':
        for i in range(len(directions)):
            direct = directions[count % len(directions)]
            if direct == 'L':
                
                curr = dic[curr][0]
            else:
                curr = dic[curr][1]
            count += 1
    return count

def search_step(seed, direct):
    if direct == 'L':
        return dic[seed][0]
    else:
        return dic[seed][1]

print(search('AAA'))

seeds = []
for k in dic.keys():
    if k[2] == "A":
        seeds.append(k)

cycles = []
for seed in seeds:
    curr = seed
    count = 0
    while curr[2] != 'Z':
        curr = search_step(curr, directions[count % len(directions)])
        count += 1
    cycles.append(count)
print(math.lcm(*cycles)) 
