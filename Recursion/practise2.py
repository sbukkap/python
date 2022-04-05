#computing power of a given number in logn time
def power(a,b):
    if b == 0:
        return 1
    elif b%2 == 0:
        return power(a*a,b/2)
    return a*power(a,b-1)
print(power(4,3))
