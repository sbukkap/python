l=[1,3,2,4,6,5]
for i in range(1,len(l)):
    temp_var=i
    j=i-1
    while j>=0:
        if l[temp_var]<l[j]:
            temp=l[j]
            l[j]=l[temp_var]
            l[temp_var]=temp
        j-=1
        temp_var-=1
print(l)
