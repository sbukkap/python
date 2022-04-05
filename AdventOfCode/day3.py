def btod(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal
f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input3.txt","r")

arr = list(map(str, f.readlines()))
arr1 = arr.copy()
"""
gamma = ''
for i in range(len(arr[0])-1):
    c0,c1 = 0,0
    for j in arr:
        if j[i] == '1':
            c1+=1
        else:
            c0+=1
    if c1>c0:
        gamma+='1'
    else:
        gamma+='0'
delta = ''
for i in gamma:
    if i  == '1':
        delta+='0'
    else:
        delta+='1'


print(btod(gamma)*btod(delta))"""


"""parrt two"""

"""for o2"""
for i in range(len(arr[0])-1):
    temp1 = []
    temp2 = []
    c0,c1 = 0,0
    for j in arr:
        if j[i] == '1':
            c1+=1
            temp1.append(j)
        else:
            c0+=1
            temp2.append(j)
    if len(temp1) == 0 or len(temp2) == 0:
        break
    if c1>=c0:
        arr = temp1
    else:
        arr = temp2

"""for co2"""
for i in range(len(arr1[0])-1):
    temp1 = []
    temp2 = []
    c0,c1 = 0,0
    for j in arr1:
        if j[i] == '1':
            c1+=1
            temp1.append(j)
        else:
            c0+=1
            temp2.append(j)
    if len(temp1) == 0 or len(temp2) == 0:
        break
    if c0<=c1:
        arr1 = temp2
    else:
        arr1 = temp1
o2 = arr[0]
co2 = arr1[0]

print(btod(o2[:len(o2)-1])*btod(co2[:len(co2)-1]))
