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
def search(target,l,ans,d):
    if target in d:
        return d[target]
    if target == '':
        return True
    for i in range(len(l)):
        x = check(l[i],target)
        if x>0 and search(target[x:],l,ans,d):
            ans+=1
    d[target] = ans
    return ans

print(search('apple',l,0,{}))
