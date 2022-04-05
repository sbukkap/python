mat=[[1,4,5,7,1],[9,8,6,2,0],[11,4,3,1,1],[6,8,9,5,0]]
r=len(mat)
c=len(mat[0])
TR=0
BR=r-1
LC=0
RC=c-1
dir='right'
l=[]

while TR<=BR and LC<=RC:
    if dir=='right':
        for i in range(LC,RC+1):
            l.append(mat[TR][i])
        TR+=1
        dir='down'
    elif dir=='down':
        for i in range(TR,BR+1):
            l.append(mat[i][RC])
        RC-=1
        dir='left'
    elif dir=='left':
        for i in range(RC,LC-1,-1):
            l.append(mat[BR][i])
        BR-=1
        dir='up'
    elif dir=='up':
        for i in range(BR,TR-1,-1):
            l.append(mat[i][LC])
        LC+=1
        dir='right'
print(l)
