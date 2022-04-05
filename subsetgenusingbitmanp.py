l = [6,1,4]

k = 1<<n
"""or k = 2**n"""


for i in range(1,k):

    for j in range(len(l)):
        if i&(1<<j):
            print(l[j],end = ' ')
    print()
