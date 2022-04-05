row,col=int(input('enter o. of rows')),int(input('enter no. of columns'))
print('enter elements')
l=[[int(input()) for i in range(col)] for j in range(row)]
row2,col2=int(input('enter o. of rows for 2nd matrix')),int(input('enter no. of columns'))
print('enter elements')
l2=[[int(input()) for i in range(col2)] for j in range(row2)]
resultant_matrix=[[0 for i in range(col2)] for j in range(row)]
if col==row2:
    for i in range(len(l)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                resultant_matrix[i][j]+=l[i][k]*l2[k][j]
    print(resultant_matrix)
else:
    print('matrix multiplicaon not possible')
