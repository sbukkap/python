"""function that returns a first valid combination that sums up to target,
ps - here i wrote len(solutions) == 2 as i needed 2 combinations(if they exist) that sum up to target
if you need only one combination , remove and len(solutions) == 2 in line 14"""
l = [1,3,4,6,4,9,7,11,13]
solutions = []
def search(state,target,nums):
    if target == 0:
        solutions.append(state.copy())
        return
    elif target<0:
        return 'Not found :-('
    for i in range(len(nums)):
        search(state+[nums[i]],target - nums[i],nums[i+1:])
        if solutions:
            return solutions
    return 'Not found :-('

print(search([],14,l))
