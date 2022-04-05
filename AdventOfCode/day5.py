"""part one"""

f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input5.txt","r")

x = list(map(str,f.readlines()))


"""take input into a matrix"""
for i in range(len(x)):
    x[i] = x[i].rstrip('\n')
mat = []


for i in x:
    t = i.split(' -> ')
    t1 = []
    for i in t:
        t1.extend(i.split(','))
    mat.append(t1)

from collections import defaultdict
d = defaultdict(int)
"""for i in mat:
    x1,y1,x2,y2 = int(i[0]),int(i[1]),int(i[2]),int(i[3])
    if x1 == x2:
        yrange = range(y1,y2+1) if y1<y2 else range(y2,y1+1)
        for i in yrange:
            d[f'{x1},{i}']+=1
    elif y1 == y2:
        xrange = range(x1,x2+1) if x1<x2 else range(x2,x1+1)
        for i in xrange:
            d[f'{i},{y1}']+=1
print(len([x for x in d.values() if x>=2]))"""


"""part two"""

for i in mat:
    x1,y1,x2,y2 = int(i[0]),int(i[1]),int(i[2]),int(i[3])
    if x1 == x2:
        yrange = range(y1,y2+1) if y1<y2 else range(y2,y1+1)
        for i in yrange:
            d[f'{x1},{i}']+=1
    elif y1 == y2:
        xrange = range(x1,x2+1) if x1<x2 else range(x2,x1+1)
        for i in xrange:
            d[f'{i},{y1}']+=1
    else:
        if abs(x1 - x2) == abs(y1 - y2):
            xrange = range(x1,x2+1) if x1<x2 else range(x1,x2 - 1,-1)
            yrange = range(y1,y2+1) if y1<y2 else range(y1,y2 - 1,-1)
            for i,j in zip(xrange,yrange):
                d[f'{i},{j}']+=1
print(len([x for x in d.values() if x>=2]))
