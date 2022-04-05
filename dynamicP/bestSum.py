l = [1,2,5,25]
solutions = []
temp = []
def search(state,target,nums):
    if target == 0:
        solutions.append(state.copy())
        return
    elif target<0:
        return
    for i in range(len(nums)):
        search(state+[nums[i]],target - nums[i],nums[i:])
        if len(solutions)==2:
            if len(solutions[-1])<=len(solutions[0]):
                solutions.pop(0)
            else:
                solutions.pop()
search([],100,l)

print(solutions)
