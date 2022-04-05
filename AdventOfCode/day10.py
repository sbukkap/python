f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input9.txt","r")

x = f.read().splitlines()

"""pts = {')':3,"]":57,"}":1197,">":25137}

d = {')':'(',']':'[','}':'{','>':'<'}
ans = 0
for k in x:
    stack = []
    for i in k:
        if i in '{([<':
            stack.append(i)
        elif d[i] == stack[-1]:
            stack.pop()
        else:
            ans+=pts[i]
            break
    print(stack)"""


"""part two"""
pts2 = {')':1,']':2,'}':3,'>':4}
d = {'(':')','[':']','{':'}','<':'>'}
d2 = {')':'(',']':'[','}':'{','>':'<'}
answers = []
for k in x:
    stack = []
    wrongseq = False
    for i in k:
        if i in '{([<':
            stack.append(i)
        elif d2[i] == stack[-1]:
            stack.pop()
        else:
            wrongseq = True
            break
    if not wrongseq:
        total = 0
        for i in stack[::-1]:
            total*=5
            total+=pts2[d[i]]
        answers.append(total)

answers.sort()

mid_i = len(answers)//2
print(len(answers))
