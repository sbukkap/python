#dynamicP approach to finding the number of ways to travek in a mxn grid if only right and
#downward direction movement is allowed..

#dynamicP method
#optimal
def grid(m,n,d):
    store_val = str(m) +','+ str(n)
    if store_val in d:
        return d[store_val]
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        x = grid(m-1,n,d) + grid(m,n-1,d)
        d[store_val] = x
        return x
#TC->  O(m*n)
#SC->  O(m+n)
print(grid(6,5,{}))
print(grid(10,9,{}))
print(grid(100,100,{})) #fails



#recursive method
#fails for large vals.....
"""def grid(m,n):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        return grid(m-1,n) + grid(m,n-1)
#TC -> O(2^(m+n))
#SC -> O(m+n)
print(grid(6,5))
print(grid(10,9))
print(grid(15,15)) #fails
"""
