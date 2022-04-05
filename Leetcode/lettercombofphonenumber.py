def letterCombinations(digits):
    final_list=[]
    k=1
    mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    for i in digits:
        if i not in '23456789':
            return []
    if len(digits)==1:
        final_list+=mapping[digits]
        return final_list
    if len(digits)==0:
        return []
    first=[]
    first+=mapping[digits[0]]
    second=mapping[digits[1]]
    def work_doer(first,second):
        temp_list=[]
        for i in first:
            for j in second:
                temp_list.append(i+j)
        temp_list2=temp_list
        if second==mapping[digits[-1]]:
            final_list=temp_list2
            return final_list
        else:
            work_doer(temp_list2,mapping[digits[k+1]])
    return work_doer(first,second)
print(letterCombinations('99'))
