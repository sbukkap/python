l=[1,2,3,4,5]
l2=['a','b','c','d','e']

for i in l:
    for j in l2:
        if j=='c':
            break
        print(j)
