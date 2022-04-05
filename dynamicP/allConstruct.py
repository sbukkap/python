l = ['ap','a','pp','p','le','e','l','appl','appl','apple']
def check(s,t):
    if len(s)>len(t):
        return -1
    c = 0
    for i in range(len(s)):
        if s[i]==t[i]:
            c+=1
        else:
            return -1
    return c
solutions = []
def search(state,target,l,solutions,d):
    if target in d:
        solutions.append(state+d[target])
        return
    if target == '':
        solutions.append(state.copy())
        return
    for i in range(len(l)):
        x = check(l[i],target)
        if x>0:
            search(state+[l[i]],target[x:],l,solutions,d)
    d[target] = state.copy()
search([],'apple',l,solutions,{})
print(solutions)
