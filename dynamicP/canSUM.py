#chek if given targetsum exists in array.
#recursive
def search(l,target):
    if target == 0:
        return True
    elif target < 0:
        return False
    for i in range(len(l)):
        if search(l[i:],target - l[i]):
            return True
    return False
print(search([7,14],14000))
#print(search([1,3,6,4,2,5,7,9],7))

#dynamicP
"""
def search(l,target,d):
    if target in d:
        return d[target]
    if target == 0:
        return True
    elif target < 0:
        return False
    for i in range(len(l)):
        if search(l[i:],target - l[i],d):
            d[target] = True
            return True
    d[target] = False
    return False

"""
