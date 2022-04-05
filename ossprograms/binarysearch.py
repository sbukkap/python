def binary_search(list,target):
    low = 0
    high=len(list)-1
    mid=int((low+high)/2)
    while mid-low>=1 or high-mid>=1:
        if list[0]==target or list[len(list)-1]==target:
            print('found')
            break
        elif list[mid]==target:
            print('numberfound')
            break
        elif list[mid]<target:
            low=mid+1
            mid=int((low+high)/2)
            continue
        elif list[mid]>target:
            high=mid
            mid=int((low+high)/2)
            continue
        else:
            print('nope')
    if list[0]==target or list[len(list)-1]==target or list[mid]==target:
        print(':)')
    else:
        print('not found :(')
binary_search([1,10,15,17,27,65],10)
