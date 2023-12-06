from aoclib import *
import os
import math


day = 5

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

inp = inp.split('\n\n')

inp = [i.split('\n') for i in inp]

for i in range(1, len(inp)):
    inp[i] = [inp[i][j].split() for j in range(1, len(inp[i]))]


for i in range(1, len(inp)):
    for j in range(len(inp[i])):
        inp[i][j] = [int(k) for k in inp[i][j]]

inp[0] = [int(j) for j in inp[0][0].split(':')[1].split()]

def mp(inp_num, inp_section):
    for i in range(len(inp_section)):
        if inp_num >= inp_section[i][1] and inp_num <= inp_section[i][1] + inp_section[i][2]:
            return inp_num - inp_section[i][1] + inp_section[i][0]
    return inp_num

def run_maps(nums, inp):
    new_nums = []
    for i in range(len(nums)):
        mapped = nums[i]
        for j in range(1, len(inp)):
            mapped = mp(mapped, inp[j])
        new_nums.append(mapped)
    return new_nums

def run_map(num, inp):
    mapped = num
    for j in range(1, len(inp)):
        mapped = mp(mapped, inp[j])
    return mapped

print("Part 1:", min(run_maps(inp[0], inp)))

# Part 2

newinp0 = []

i = 0
while i < len(inp[0]):
    newinp0.append([inp[0][i], inp[0][i+1]])
    i += 2

inp[0] = newinp0

min_found = math.inf

approxranges = []

for i in range(len(inp[0])):
    for j in range(inp[0][i][0], inp[0][i][0] + inp[0][i][1]+1, int(math.sqrt(inp[0][i][1]))):
        approxranges.append(j)

maps = run_maps(approxranges, inp)
minimum = min(maps)
min_index = maps.index(minimum)
approx_minimum_seed = approxranges[min_index]

for i in inp[0]:
    if approx_minimum_seed <= i[0] + i[1] and approx_minimum_seed >= i[0]:
        inp[0] = i

print("Starting from approximate seed: ", approx_minimum_seed)
print("Using search parameters: ", approx_minimum_seed - int(math.sqrt(inp[0][1])), ' to ', approx_minimum_seed + int(math.sqrt(inp[0][1])))

for j in range(approx_minimum_seed - int(math.sqrt(inp[0][1])), approx_minimum_seed + int(math.sqrt(inp[0][1]))):
    if j % 1000000 == 0: print(f"We're at {j - inp[0][0]} out of, {inp[0][1]}, which is {round((j - inp[0][0])/inp[0][1]*100, 2)}%")
    if run_map(j, inp) < min_found:
        min_found = run_map(j, inp)

print('Part 2:', min_found)
