
import os

day = 6

def read_input(filename):
    with open(filename) as f:
        lines = f.read()
    return lines

inp = read_input(f'Puzzle{day}.txt')

times = [42, 68, 69, 85]
distances = [284, 1005, 1122, 1341]


def travel_dist(hold_time, tot_time):
    return (tot_time - hold_time) * hold_time

x = 1
for time in times:
    ways = 0
    for t in range(time):
        if travel_dist(t, time) > distances[times.index(time)]:
            ways += 1
    x *= ways

print(x)

ways = 0

time = 42686985
distance = 284100511221341

for t in range(time):
    if travel_dist(t, time) > distance:
        ways += 1

print(ways)