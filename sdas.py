class Solution:
    def bruh69(self, nums):
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if i*2 in d:
                minval=min(d[i],d[i*2])
                d[i]-=minval
                d[i*2]-=minval
                r+=[i]*minval
        for i in d:
            if d[i]!=0:
                return []
        return r
s = Solution()
print(s.bruh69([1,3,4,2,6,8]))
