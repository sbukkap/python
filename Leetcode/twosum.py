dict={}
for i in range(len(nums)):
    y=target-nums[i]
    if nums[i] in dict:
        return [dict[nums[i]],i]
    else:
        dict[y]=i
