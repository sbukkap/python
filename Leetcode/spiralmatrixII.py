n=int(input('enter n value'))
spmat=[[0 for i in range(n)] for j in range(n)]
tr=0
br=len(spmat)-1
lc=0
rc=len(spmat[0])-1
dir='right'
number=1
while tr<=br and lc<=rc:
    if dir=='right':
        for i in range(lc,rc+1):
            spmat[tr][i]=number
            number+=1
        dir='down'
        tr+=1
    elif dir=='down':
        for i in range(tr,br+1):
            spmat[i][rc]=number
            number+=1
        dir='left'
        rc-=1
    elif dir=='left':
        for i in range(rc,lc-1,-1):
            spmat[br][i]=number
            number+=1
        dir='up'
        br-=1
    elif dir=='up':
        for i in range(br,tr-1,-1):
            spmat[i][lc]=number
            number+=1
        dir='right'
        lc+=1
for i in spmat:
    print(i,end=)
