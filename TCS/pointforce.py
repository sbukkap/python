def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
f,p1,p2 = map(int, input().split())
d = set()
for i in range(p1,p2+1):
    if is_prime(i):
        d.add(i)

def work(f,p1,p2,d):
    t = [-1,-1]
    min = 10000000000000
    for i in range(p1,p2):
        if i in d:
            continue
        else:
            for j in range(i+1,p2+1):
                if j not in d:
                    val = (i*j)/((j-i)**2)
                    if val>=f and val <= min:
                        min = val
                        t = [i,j]
    return t
x,y = work(f,p1,p2,d)
if x!=-1 and y!=-1:
    print(x,y)
else:
    print('None')
