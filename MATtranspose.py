r,c=int(input('enter no. of rows')),int(input('enter no. of columns'))

print('enter matrix elements')

matrix1=[[int(input()) for i in range(c)] for j in range(r)]

print('your mattrix is ')

for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end='  ')
    print()

transpose=[[0 for i in range(r)] for j in range(c)]

transpose_rows = len(transpose)
transpose_columns = len(transpose[0])

for i in range(transpose_rows):
    for j in range(transpose_columns):
        transpose[i][j] = matrix1[j][i]

print('the transposed matrix is ')

for i in range(transpose_rows):
    for j in range(transpose_columns):
        print(transpose[i][j],end=' ')
    print()
