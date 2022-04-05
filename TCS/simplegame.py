mat = []
for i in range(3):
    x = input()
    temp = []
    for i in x:
        temp.append(i)
    mat.append(temp)

def valid(board):
    xc = 0
    oc = 0
    r = [0]*3
    c = [0]*3
    d = 0
    a = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                oc += 1
                r[i] -= 1
                c[j] -= 1
                if i == j:
                    d -=1
                if i +j  == 2:
                    a -= 1
            elif board[i][j] == "X":
                xc += 1
                r[i] += 1
                c[j] += 1
                if i == j:
                    d +=1
                if i + j  == 2:
                    a += 1
    if xc < oc or xc > oc+1:
        return False
    cl = r + c + [d] + [a]
    cx = sum(1 if ele == 3 else 0 for ele in cl)
    co = sum(1 if ele == -3 else 0 for ele in cl)

    if cx and co:
        return False

    elif cx and xc == oc:
        return False

    elif co and xc == oc + 1:
        return False
    else:
        return True
if valid(mat):
    print('YES')
else:
    print('NO')
