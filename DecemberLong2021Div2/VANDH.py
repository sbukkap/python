# cook your dish here


for i in range(int(input())):
    h,v = map(int, input().split())

    def work():
        s = ''
        if h == v:
            s = '01'*(h+1)
        elif h>v:
            v_prod = h - 1
            c = 0
            for i in range(h):
                s+='01'
                if c!=(v_prod-v):
                    s+='0'
                    c+=1
            s+='0'
        else:
            h_prod = v - 1
            c = 0
            for i in range(v):
                s+='10'
                if c!=(h_prod-h):
                    s+='1'
                    c+=1
            s+='1'
        return s,len(s)
    x,y = work()
    print(y)
    print(x)
