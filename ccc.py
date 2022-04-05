"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
def sum_3(nums):
    map={}
    final_list=[]
    for i in range(len(nums)):
        target_element=nums[i]
        for j in range(len(nums)):
            if nums[j]!=target_element:
                y=target_element-nums[j]
                if nums[j] in map:
                    final_list.append([y,target_element,nums[j]])
                else:
                    map[y]=j
    return final_list
print(sum_3([-1,0,1,2,-1,-4]))
