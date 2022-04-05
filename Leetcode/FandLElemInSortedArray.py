def binary_search(arr, x):
    def LefMostFinder(arr,x):
        leftmostindex=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                leftmostindex=mid
                high=mid-1
            elif arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
        return leftmostindex
    def RightMostFinder(arr,x):
        rightmostindex=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                rightmostindex=mid
                low=mid+1
            elif arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
        return rightmostindex
    x,y=LefMostFinder(arr,x),RightMostFinder(arr,x)
    result=[x,y]
    return result
print(binary_search([5],5))
