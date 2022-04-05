"""
From the givven array,find the minimum-sized subarray whose sum of elements is greater than or equal to 8(or k)
"""
def minimum_size(l,k):
    windowStart=0
    current_sum=0
    min_size=100000
    for windowEnd in range(len(l)):
        if min_size==1:
            break
        current_sum+=l[windowEnd]
        while current_sum>=k:
            if (windowEnd-windowStart)+1<min_size:
                min_size=(windowEnd-windowStart)+1
            current_sum-=l[windowStart]
            windowStart+=1
    return min_size
print(minimum_size([4,2,2,5,4,7,8,3,5],14))
