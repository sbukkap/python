mod = 998244353

def apowb(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    ret = apowb(a,b//2)
    if b%2 == 0:
        return (ret * ret)%mod
    else:
        return ((ret * ret)%mod*a)%mod
print(apowb(2,8))
