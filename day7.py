from aoclib import *
import os

day = 7

if not os.path.isfile(f'Puzzle{day}.txt'):
    grab(day)

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

powers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
powers2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

powers.reverse()
powers2.reverse()

inp = read_input(f'Puzzle{day}.txt')



inp = [j.strip().split() for j in inp.split('\n')]

def score_1(bidwinpair, second = True):
    kinds = {}
    score = 0.0
    
    for i in range(len(bidwinpair[0])):
        if bidwinpair[0][i] in kinds:
            kinds[bidwinpair[0][i]] += 1
        else:
            kinds[bidwinpair[0][i]] = 1
        if second: score += powers.index(bidwinpair[0][i]) / (100.0 ** (i+1)) 

    
    if 5 in kinds.values():
        score += 7
    elif 4 in kinds.values():
        score += 6
    elif 3 in kinds.values() and 2 in kinds.values():
        score += 5
    elif 3 in kinds.values():
        score += 4
    elif len(kinds) == 5:
        score += 1
    elif 2 in kinds.values() and len(kinds) == 3:
        score += 3
    else: score +=2

    return score


inp.sort(key=score_1)

totscore = 0

for i in range(len(inp)):
    totscore += (1+i) * int(inp[i][1])

print(totscore)


def score_2(bidwinpair):
    origscore = 0.0
    for i in range(len(bidwinpair[0])):
        origscore += powers2.index(bidwinpair[0][i]) / (100.0 ** (i+1)) 

    score = 0

    for i in powers2:
        temp = bidwinpair.copy()
        temp[0] = temp[0].replace('J', i)
        if score_1(temp) > score:
            score = score_1(temp, False)
    return score + origscore

inp.sort(key=score_2)


totscore = 0

for i in range(len(inp)):
    totscore += (1+i) * int(inp[i][1])

print(totscore)
