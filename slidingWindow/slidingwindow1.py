"""
using sliding window approach for finding the max possible sum of elements of a subarray of len 3(or k) in a given subarray
https://www.youtube.com/watch?v=MK-NZ4hN7rs
"""
def max_sum_finder(l,k):
    max_sum=-1000
    current_sum=0
    for i in range(len(l)):
        current_sum+=l[i]
        if i>=k-1:
            if current_sum>max_sum:
                max_sum=current_sum
            current_sum-=l[i-(k-1)]
    return max_sum
print(max_sum_finder([2,7,4,2,5,6,0,6,3,6],4))
