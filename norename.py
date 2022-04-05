matrix1 = [[1],[2]]

l=len(matrix1[0])
for i in range(l):
    for j in range(i,l):
        matrix1[i][j],matrix1[j][i] = matrix1[j][i],matrix1[i][j]
print(matrix1)
