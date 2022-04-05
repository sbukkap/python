"""
c = set(range(4))
c.discard(-1)
print(c)
"""
"""
c = [1,2,3,4]

c.remove(0)
print(c)
"""
class Solution:
    def combine(self,n,k):
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
s = Solution()

print(s.combine(4,3))
