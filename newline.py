class Solution:
    def permute(self, nums):
        solutions = []
        state = []
        l = len(nums)
        def get_candidates(nums,state,i):
            if not state:
                return nums
            return nums[:i]+nums[i+1:]
        def search(nums,state,i):
            print(state)
            if len(state) == l:
                solutions.append(state.copy())
                return
            for c in get_candidates(nums,state,i):
                state.append(c)
                search(nums,state,i+1)
                state.pop()
        search(nums,[],-1)
        return solutions
s = Solution()
print(s.permute([1,2,3]))
