def floodfill(matrix,r,c,tofill,prevfill):
    rows=len(matrix)
    col=len(matrix[0])
    if r<0 or c<0 or r>=rows or c>=col:
        return
    if matrix[r][c] != prevfill:
        return
    matrix[r][c] = tofill
    floodfill(matrix,r+1,c,tofill,prevfill)
    floodfill(matrix,r-1,c,tofill,prevfill)
    floodfill(matrix,r,c+1,tofill,prevfill)
    floodfill(matrix,r,c-1,tofill,prevfill)
matrix= [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0],
[1,0,0,1,1,0,1,1],
[1,2,2,2,2,0,1,0],
[1,1,1,2,2,0,1,0],
[1,1,1,2,2,2,2,0],
[1,1,1,1,1,2,1,1],
[1,1,1,1,1,2,2,1]
]
floodfill(matrix,7,7,3,1)
for i in matrix:
    print(i,end='\n')
