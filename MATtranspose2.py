mat = [[1,2,3],[4,5,6],[7,8,9]]
l = len(mat[0])
for i in range(l):
    for j in range(i,l):
        mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
for i in mat:
    for j in i:
        print(j,end=' ')
    print()
