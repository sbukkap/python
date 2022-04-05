def reverse(x):
    list=str(x)
    list2=''
    if x>=0:
        for i in range(1,len(list)+1):
            list2=list2+list[-i]
        print(list2)
    else:
        list2=list2+'-'
        for i in range(1,len(list)):
            list2=list2+list[-i]
        print(list2)
reverse(0)
