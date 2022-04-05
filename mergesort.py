"""this function merges two sorted lists into a single sorted list"""
def merge(l1,l2):
    ln1 = len(l1)
    ln2 = len(l2)
    result = []
    i,j = 0,0
    while i<ln1 or j<ln2:
        if i == ln1:
            result.extend(l2[j:])
            break
        if j == ln2:
            result.extend(l1[i:])
            break
        if l1[i] < l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j+=1
    return result
def mergeSort(l):
    if len(l) == 1: #base case
        return l
    mid = len(l)//2
    return merge(mergeSort(l[:mid]),mergeSort(l[mid:]))
print(mergeSort([7,5,3,8,9,1,6]))
