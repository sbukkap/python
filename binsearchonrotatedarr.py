arr = [15,17,21,1,3,5,7,12,13]

def bins(arr,key):
    fin = arr[-1]
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < fin and key<fin:
            low = mid+1
        elif arr[mid] > fin and key < fin:
            low = mid+1
        elif arr[mid] < fin and key>fin:
            high = mid-1
        elif arr[mid]>fin and key>fin:
            high = mid-1
    return -1
print(bins(arr,2))
