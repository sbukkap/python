"""file = open("C:/Users/iamop/OneDrive/Desktop/AOC/input2.txt",'r')

arr = list(map(str, file.readlines()))

final_h,final_d = 0,0


for i in arr:
    _,d = i.split()
    if i[0] == 'f':
        final_h+=int(d)
    elif i[0] == 'u':
        final_d-=int(d)
    else:
        final_d+=int(d)
print(final_h*final_d)
"""
"""part two"""
file = open("C:/Users/iamop/OneDrive/Desktop/AOC/input2.txt",'r')

arr = list(map(str, file.readlines()))
final_h,final_d = 0,0
aim = 0

for i in arr:
    _,d = i.split()
    if i[0] == 'f':
        final_h+=int(d)
        final_d += int(d)*aim
    elif i[0] == 'u':
        aim-=int(d)
    else:
        aim+=int(d)
print(final_h*final_d)
