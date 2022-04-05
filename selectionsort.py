l=[6,5,4,3,2]
min_index=0
step=0
for i in range(len(l)):
    min=l[i]
    for j in range(i+1,len(l)):
        if l[j]<min:
            new_min_found=True
            min=l[j]
            min_index=j
            step+=1
    if new_min_found==True:
        temp=l[i]
        l[i]=l[min_index]
        l[min_index]=temp
        new_min_found=False
        step+=1
print(l)
print(step)
