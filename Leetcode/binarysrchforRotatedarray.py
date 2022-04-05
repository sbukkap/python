def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid-1]<arr[mid]<arr[mid+1]:
            if arr[mid]<x:
                low = mid + 1
            elif arr[mid]>x:
                high = mid - 1
            else:
                return mid
        else:
            if x<=arr[-1]:
                low=mid+1
            elif x>=arr[0]:
                high=mid-1
            else:
                return mid
    return -1
print(binary_search([4,5,6,7,0,1,2],0))
