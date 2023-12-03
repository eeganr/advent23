import math
def is_prime(n):
    # REQUIRES MATH MODULE
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    a=int(math.sqrt(n))+1
    for i in range(3,a,2):
        if n%i==0:
            return False
    return True

class Short:
    def __init__(self,nodes,connections):
        self.nodes=nodes
        self.cons=connections
    def get(self,node):
        return self.nodes.index(node)
    def find_shortest(self,node1,node2):
        try:
            self.get_dist
            exist=True
        except:
            exist=False
        meta=dict()
        for i in self.nodes:
            meta[i]=None
        meta[node1]=0
        if not exist:
            queue=[node1]
        else:
            queue=[(self.get_dist(node1,node2),node1)]
        while queue:
            if exist:
                dist,node=queue.pop(0)
            else:
                node=queue.pop(0)
            poss=self.cons[node]
            current=meta[node]
            for i in poss:
                c=self.get_cost(node,i)
                if meta[i]==None:
                    if exist:
                        queue.append((self.get_dist(i,node2),i))
                    else:
                        queue.append(i)
                    meta[i]=current+c
                elif meta[i]>current+c:
                    if exist:
                        queue.append((self.get_dist(i,node2),i))
                    else:
                        queue.append(i)
                    meta[i]=current+c
            if exist:
                queue.sort()
        return meta[node2]
    def get_cost(self,node1,node2):
        return 1

def long_function_name_XzWOUpDw0T(x,y):
    if x<y:
        return 1
    elif x>y:
        return -1
    return 0

def QUICKSORT(vals,cmp=None):
    if cmp==None:
        cmp=long_function_name_XzWOUpDw0T
    less=[]
    equal=[]
    more=[]
    if len(vals)>1:
        a=vals[0]
        b=vals[int(len(vals)/2)]
        c=vals[-1]
        ab=cmp(a,b)
        ac=cmp(a,c)
        bc=cmp(b,c)
        if ab==1 and bc==1 or ab==-1 and bc==-1:
            pivot=b
        elif ac==1 and bc==-1 or ac==-1 and bc==1:
            pivot=c
        else:
            pivot=a
        for i in vals:
            a=cmp(i,pivot)
            if a==1:
                less.append(i)
            elif a==-1:
                more.append(i)
            else:
                equal.append(i)
        return QUICKSORT(less,cmp)+equal+QUICKSORT(more,cmp)
    else:
        return vals
            
