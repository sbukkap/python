#1
val = 3
"""
if val == 0:
    print('yes')
else:
    print('no')
"""
x = 'yes' if val == 0 else 'no'
print(x)


#2 : Using enumerate
l = [1,2,3,4,5,6]

for index,val in enumerate(l,start=1):
    print(index,val)

#3 zip function
"""zip function can be used to traverse multiple liss at once :) """
l = [1,2,3,4,5]
l1 = ['a','b','c','d','e']

for i,j in zip(l,l1):
    print(i,j)

#4
"""in python , _ can be used as a name to a list,str,etc.....which we are not gonna use anywhere else
in the progrm"""
"""now lets say we wanted to unpack values and we only are concerned with a ...then we just ignore
b using _ ..even python understands that it is a variable to be ignored"""
a,_ = [1,2]

"""also"""
a,b,*c = [1,2,3,4,5]
#here a will be 1, b 2 , and c will be the remaining list...note that we used * for that

a,b,*_ = [1,2,3,4,5,6,7]


#5
