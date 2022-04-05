# cook your dish here


for i in range(int(input())):
    h,v = map(int, input().split())

    def work():
        if h == v:
            s = '01'*(h+1)
        elif h>v:
            s = '010'*h
            if v == 0:
                return s
            c = 0
            for i in range(len(s)-1):
                if s[i] == s[i+1] == '0':
                    s = s.replace(s[i],'x')
                    c+=1
                if c == v:
                    return s
            return s
        else:
            s = '101'*v
            if h == 0:
                return s
            c = 0
            for i in range(len(s)-1):
                if s[i] == s[i+1] == '1':
                    s = s.replace(s[i],'x')
                    c+=1
                if c == h:
                    return s
            return s
    x = work()
    p = ''
    for i in x:
        if i!='x':
            p+=i
    print(p)
