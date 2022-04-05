class Solution:
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions = []
        state = []
        self.search(state,k,n,solutions)
        return solutions
    def search(self,state,k,n,solutions):
        if self.is_valid(state,k):
            solutions.append(state.copy())
            return
        for i in self.get_candidates(state,n):
            state.append(i)
            self.search(state,k,n,solutions)
            state.pop()
    def is_valid(self,state,k):
        return len(state) == k
    def get_candidates(self,state,n):
        if not state:
            return range(1,n+1)
        p = list(range(1,n+1))
        z = state[-1]-1
        return p[z+1:]
    """
    def combine(self, n, k):
        solutions = []
        state = []
        def search(i,n,k):
            print(state)
            if len(state) == k:
                solutions.append(state.copy())
                return
            for c in range(i,n+1):
                state.append(c)
                search(c+1,n,k)
                state.pop()
        search(1,n,k)
        return solutions
"""did this on my own(not totally) yayyy!"""
"""but theres a better solution"""
#https://www.youtube.com/watch?v=q0s6m7AiM7o
s = Solution()
print(s.combine(4,2))
