j=0
nums=[2,3,4,3,3,5,6,7,3]
val=3
for i in nums:
    if i!=val:
        nums.insert(j,i)
        j+=1
print(nums)
"""
