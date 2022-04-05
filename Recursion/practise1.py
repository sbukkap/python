"""from Apni kaksha recursion practise"""
#computing power of a given number
def power(a,b):
    if b == 0:
        return 1
    return a*power(a,b-1)
print(power(4,3))
