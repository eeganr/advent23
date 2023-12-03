from aoclib import *
#cmds
#itertools.permutations, itertools.product
#x=defaultdict(list), x.append(0)
#x=Counter('asdfa'), x.most_common(3) -> 3 most common as [('a',2) ... ]
#x=deque(), x.append(0), x.popleft(), x.popright()
#shortest path: Short(nodes, connections).find_shortest(node1,node2)
#sort: QUICKSORT(vals,cmp=None) cmp is custom comparison to sort by

day=0
#day=grab(day)
with open(f"Puzzle{day}.txt",'r') as r:
    lines=r.read().split('\n')

#lines=[int(i) for i in lines]
lines=[str(i) for i in lines]
'''
lines="""""".split('\n')
#'''
print(len(lines))
#x is output

def parse(x):

    f=0
    x=0
    A=[]
    total=0
    vals=[]

    for i in lines:f+=parse(i)




    x=f
    clipboard.copy(x)
    print(x)
