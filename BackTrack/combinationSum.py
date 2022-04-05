def is_valid(state,target):
    sum = 0
    for i in state:
        sum+=i
    return sum
def search(solutions,candidates,state,target):
    if is_valid(state,target) == target:
        solutions.append(state.copy())
        return
    elif is_valid(state,target) > target:
        return
    for i in candidates:
        state.append(i)
        search(solutions,candidates,state,target)
        state.pop()
def comb(candidates,target):
    solutions=[]
    state = []
    search(solutions,candidates,state,target)
    result = []
    for i in solutions:
        i.sort()
    for i in solutions:
        if i not in result:
             result.append(i)
    return result
print(comb([2,7,6,3,5,1],9))
