f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input8.txt","r")

x = f.read().splitlines()
mat = []
for i in x:
    mat.append([int(x) for x in i])

r = len(mat)-1
c = len(mat[0])-1
sum = 0
for i in range(r+1):
    for j in range(c+1):
        elem = mat[i][j]
        if i == 0 and j == 0:
            sum += elem+1 if elem<mat[i][j+1] and elem<mat[i+1][j] else 0
        elif i == r and j == c:
            sum+=elem+1 if elem<mat[i][j-1] and elem<mat[i-1][j] else 0
        elif i == r and j == 0:
            sum+=elem+1 if elem<mat[i][j+1] and elem<mat[i-1][j] else 0
        elif i == 0 and j == c:
            sum+=elem+1 if elem<mat[i][j-1] and elem<mat[i+1][j] else 0
        elif i != 0 and j == c:
            sum+=elem+1 if elem<mat[i][j-1] and elem<mat[i-1][j] and elem<mat[i+1][j] else 0
        elif i == 0 and j!=c:
            sum+=elem+1 if elem<mat[i][j-1] and elem<mat[i+1][j] and elem<mat[i][j+1] else 0
        elif i != r and j == 0:
            sum+=elem+1 if elem<mat[i][j+1] and elem<mat[i-1][j] and elem<mat[i+1][j] else 0
        elif i == r and j != 0:
            sum+=elem+1 if elem<mat[i][j-1] and elem<mat[i-1][j] and elem<mat[i][j+1] else 0
        else:
            sum += elem+1 if elem<mat[i][j+1] and elem<mat[i+1][j] and elem<mat[i-1][j] and elem<mat[i][j-1] else 0
print(sum)
