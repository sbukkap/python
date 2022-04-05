ini = int(input())
jc = int(input())
cc = int(input())
m,n = map(int, input().split())
mat = []
for i in range(m):
    mat.append(input())
coins = [0]*n
hurdles = [0]*n
coins2 = [0]*n
for i in range(n):
    firstcoin = False
    firsthurdle = False
    for j in range(m):
        if mat[j][i] == 'C':
            if firstcoin == False:
                heightfc = j
                firstcoin = True
            coins[i]+=1
            coins2[i] = heightfc
        elif mat[j][i] == 'H' and firsthurdle == False:
            heightfh = j
            firsthurdle = True
            hole = 0
            for x in range(j,m):
                if mat[x][i] == '0':
                    hole = x
                    break
            if hole!=0:
                heightfh = hole+1
            hurdles[i] = heightfh

def mainn(ini):
    for i in range(len(coins)):
        if ini<=0:
            return i-1
        #ini = ini - rf +coins[i]*cc - (m-coins2[i])*jc - jc*(hurdles[i])
        if coins[i]!=0:
            ini+=coins[i]*cc
            ini-=(m-coins2[i]-1)*jc
        else:
            ini-=1
        if hurdles[i]!=0:
            ini-=(m-hurdles[i])*jc
    return ini
print(mainn(ini))
print(hurdles)
