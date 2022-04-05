def bruh(r,c,mat,m,n):
    ans = 0
    if r>0 and mat[r-1][c]==1:
        ans+=1
    if r<m-1 and mat[r+1][c]==1:
        ans+=1
    if c>0 and mat[r][c-1]==1:
        ans+=1
    if c<n-1 and mat[r][c+1]==1:
        ans+=1
    if r>0 and c>0 and mat[r-1][c-1]==1:
        ans+=1
    if r<m-1 and c>0 and mat[r+1][c-1]==1:
        ans+=1
    if r<m-1 and c<n-1 and mat[r+1][c+1]==1:
        ans+=1
    if r>0 and c<n-1 and mat[r-1][c+1]==1:
        ans+=1
    return ans
def dist_calc(r,c):
    if r == c:
        dist = r-1
    elif r<c:
        dist = (r-1) + c-(1+(r-1))
    else:
        dist = (c-1) + r-(1+(c-1))
    return dist

for i in range(int(input())):
    m,n = map(int, input().split())

    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))
    mat[0][0] = -1
    maxx = [0]
    res = []
    res_init = False

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                x = bruh(i,j,mat,m,n)
                if x>maxx[0]:
                    maxx = [-1]
                    maxx[0] = x
                    res = [i,j]
                    res_init = True
                elif x == maxx[0] and res_init == True:
                    if dist_calc(i,j)<dist_calc(res[0],res[1]):
                        res = [i,j]
                    elif dist_calc(i,j)==dist_calc(res[0],res[1]):
                        maxx.append(maxx[0])

    if len(maxx)>1:
        print("Polygamy not allowed")
    elif not res:
        print("No suitable girl found")
    else:
        print(f"{res[0]+1}:{res[1]+1}:{maxx[0]}")
