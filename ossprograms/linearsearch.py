l=[2,3,4,5,6,7,8,9]
flag=0
x=int(input('enter an element to be searched'))
for i in l:
    if x==i:
        flag=1
        ind=l.index(i)
    else:
        continue
if flag==1:
    print(f'element found at index {ind}')
else:
    print('element not found')
