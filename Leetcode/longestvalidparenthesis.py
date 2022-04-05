
"""
hard
using two stacks char stack and index stack
idea from yt
link : https://www.youtube.com/watch?v=qC5DGX0CPFA&t=425s
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        char_stack=['a']
        ind_stack=[-1] #index stack
        max_length=[]
        map={')':'('}
        for i in range(len(s)):
            if s[i] in map.values():
                char_stack.append(s[i])
                ind_stack.append(i)
            elif map[s[i]]==char_stack[-1]:
                ind_stack.pop()
                max_length.append(i-ind_stack[-1])
                char_stack.pop()
            else:
                ind_stack.append(i)
        if len(max_length)==0:
            return 0
        else:
            return max(max_length)
