l = [["#",".","*","."],["#","#","*","."]]
for i in l:
    rock = -1
    obstacle=-2
    for j in range(len(l[0])):
        if i[j] == '#' and rock == -1:
            rock = j
        elif i[j] == '.':
            if not (rock<obstacle<j):
                i[j] = '#'
                i[rock] = '.'
                rock+=1
            else:
                rock = -1
        elif i[j] == '*':
            obstacle = j
            rock = -1
print(l)
