leftarr=[]
rightarr=[]
def partitioner(arr):
    first=0
    last=len(arr)
    pivot=(first+last)/2
    for i in range(len(arr)):
        if arr[i]<pivot:
            leftarr.append(arr[i])
        elif i!=0 and arr[i]==pivot:
            continue
        elif arr[0]==pivot:
            continue
        elif arr[len(arr)-1]==pivot:
            continue
        else:
            rightarr.append(arr[i])
    return leftarr,pivot,rightarr
def quicksort(arr):
    leftarr,pivot,rightarr=partitioner(arr)
    if len(leftarr)==2:
        if leftarr[0]>leftarr[1]:
            temp=leftarr[0]
            leftarr[0]=leftarr[1]
            leftarr[1]=temp
    elif len(leftarr)==1:
        leftarr=leftarr[0]
    elif len(leftarr)==0:
        leftarr=[]
    else:
        quicksort(leftarr)
    if len(rightarr)==2:
        if rightarr[0]>rightarr[1]:
            tempp=rightarr[0]
            rightarr[0]=rightarr[1]
            rightarr[1]=tempp
    elif len(rightarr)==1:
        rightarr=rightarr[0]
    elif len(rightarr)==0:
        rightarr=[]
    else:
        quicksort(rightarr)
    return leftarr+pivot+rightarr
d=quicksort([1,6,2,5,3,4])
print(d)
