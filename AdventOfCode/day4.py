"""part one"""
def checker(matrix):
    #row checking:
    def r_check():
        for i in matrix:
            c = 0
            for j in i:
                if j == 'x':
                    c+=1
            if c == 5:
                return True
        return False

    def c_check():
        for i in range(len(matrix[0])):
            c = 0
            for j in matrix:
                if j[i] == 'x':
                    c+=1
            if c == 5:
                return True
        return False
    if r_check() or c_check():
        return True
    return False

#open file
f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input4.txt","r")

#read lines
bruh = list(map(str, f.readlines()))

#add all the moves or marking numbers into "moves" list
moves = []
for i in bruh[:2]:
    moves.extend(i.split(','))
#since last two values were x\n and \n.....adjusted them
moves.pop()
x = moves[-1]
moves[-1] = x[:len(x)-1]


#part two
#prepare a 2d array called "mat "
mat = []
for i in bruh[2:]:
    temp = []
    temp.extend(i.split())
    mat.append(temp)

#i used the "shift " array here to mark all the values of empty lists in mat
shift = []
for i in range(5,len(mat),6):
    shift.append(i)
shift.append(len(mat))

#work is the main function that takes in "mat" 2d array as input and does the number marking as we do in bingo....whenever any row or any column is filled it returns that matrix.
def work(mat):
    j = 0
    c = 0
    for i in moves:
        while j < len(mat):
            if i in mat[j]:
                x = mat[j].index(i)
                save_val = mat[j][x]
                mat[j][x] = 'x'
                for k in range(len(shift)):
                    if j<shift[k]:
                        j = shift[k]+1
                        y = shift[k-1] if k!=0 else -1
                        break
                m = mat[y+1:j-1]
                if checker(m):
                    return m,save_val
            else:
                j+=1
        j = 0

#print the required value now....as we have bingo matrix with us.
bingo_matrix,last_num = work(mat)
sum = 0
for i in bingo_matrix:
    for j in i:
        if j!='x':
            sum+=int(j)

print(sum*int(last_num))

"""part two"""
#this function checks if the supplied matrix has bingo in it
def checker(matrix):
    #row checking:
    def r_check():
        for i in matrix:
            c = 0
            for j in i:
                if j == 'x':
                    c+=1
            if c == 5:
                return True
        return False

    def c_check():
        for i in range(len(matrix[0])):
            c = 0
            for j in matrix:
                if j[i] == 'x':
                    c+=1
            if c == 5:
                return True
        return False
    if r_check() or c_check():
        return True
    return False

#open file
f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input4.txt","r")

#read lines
bruh = list(map(str, f.readlines()))

#add all the moves or marking numbers into "moves" list
moves = []
for i in bruh[:2]:
    moves.extend(i.split(','))
#since last two values were x\n and \n.....adjusted them
moves.pop()
x = moves[-1]
moves[-1] = x[:len(x)-1]


#part two
#prepare a 2d array called "mat "
mat = []
for i in bruh[2:]:
    temp = []
    temp.extend(i.split())
    mat.append(temp)

#i used the "shift " array here to mark all the values of empty lists in mat
shift = []
for i in range(5,len(mat),6):
    shift.append(i)
shift.append(len(mat))

#work is the main function that takes in "mat" 2d array as input and does the number marking as we do in bingo....whenever any row or any column is filled it returns that matrix.
def work(mat):
    j = 0
    c = 0
    for i in moves:
        while j < len(mat):
            if i in mat[j]:
                x = mat[j].index(i)
                save_val = mat[j][x]
                mat[j][x] = 'x'
                for k in range(len(shift)):
                    if j<shift[k]:
                        j = shift[k]+1
                        y = shift[k-1] if k!=0 else -1
                        break
                m = mat[y+1:j-1]
                if checker(m) and m[0][0]!='c':
                    c+=1
                    if c == 100:
                        return (m,save_val)
                    m[0][0] = 'c'
            else:
                j+=1
        j = 0

#print the required value now....as we have bingo matrix with us.
bingo_matrix,last_num = work(mat)
sum = 0
for i in bingo_matrix:
    for j in i:
        if j!='x':
            sum+=int(j)

print(sum*int(last_num))
