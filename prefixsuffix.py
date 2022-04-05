s = input()
c = 0
def fun(s,c):
    res = [0]
    i = 0
    j = len(s)-1
    while i<j:
        if s[:i+1] == s[j:]:
            c+=1
            res.append(c)
        else:
            c+=1
        j-=1
        i+=1
    return max(res)
print(fun(s,0))
        
