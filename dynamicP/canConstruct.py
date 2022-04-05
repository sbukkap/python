l = ['abc','abc','def','c','e','zxy']
target = 'ecap'
"""def search(state,l):
    if state == target:
        return True
    if len(state)>len(target):
        return False
    for i in range(len(l)):
        if search(state+l[i],l):
            return True
    return False
print(search('',l))"""
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
l = ['abc','bc','la','o','xm','xa']

def search(target,l,d):
    if target in d:
        return d[target]
    if target == '':
        return True
    for i in range(len(l)):
        x = check(l[i],target)
        if x>0 and search(target[x:],l,d) == True:
            d[target] = True  #store the same value in dict. before returning
            return True
    d[target] = False
    return False
print(search('xmxaxaabcbcla',l,{}))
