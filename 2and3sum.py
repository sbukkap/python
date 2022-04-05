def twosum(l,target):
    d = {}
    for i in range(len(l)):
        y = target - l[i]
        if l[i] in d:
            return [d[l[i]],i]
        else:
            d[y] = i
#print(twosum([3,5,9,2,11],13))

def threesum(l,target):
    res = []
    l.sort()
    for i in range(len(l)-2):
        if i!=0 and l[i] == l[i-1]:#corner case 1
            continue
        to_find = -l[i]
        low = i+1
        high = len(l)-1
        while low<high:
            sum = l[low]+l[high]
            if sum == to_find:
                res.append([l[i],l[low],l[high]])
                while low<high and l[low]==l[low+1]:
                    low+=1
                while low<high and l[high]==l[high-1]:
                    high-=1
                low+=1
                high-=1
            elif sum>to_find:
                high-=1
            else:
                low+=1
    return res
    """
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        target = nums[i]

        #corne case 1
        if i!=0 and nums[i]==nums[i-1]:
            continue

        to_find = -target

        low = i+1
        high = len(nums)-1

        while low<high:
            sum = nums[low]+nums[high]

            if sum == to_find:
                res.append([nums[low],nums[high],target])

                #corner case 2
                while low<high and nums[low] == nums[low+1]:
                    low+=1
                while low<high and nums[high] == nums[high-1]:
                    high-=1
                low+=1
                high-=1

            elif sum < to_find:
                low+=1
            elif sum > to_find:
                high-=1
    return res
    """
print(threesum([-1,0,1,2,-1,-4],0))
