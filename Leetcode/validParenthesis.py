"""
Runtime: 1028 ms, faster than 5.60% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 32.97% of Python3 online submissions for Valid Parentheses.
Check YT for better solution :)
link : https://www.youtube.com/watch?v=lNYozout6FM
"""

class Solution:
    def isValid(self, s: str) -> bool:
        map={'}':'{',']':'[',')':'('}
        if len(s)%2!=0:
            return False
        i,j=0,1
        while j<len(s):
            try:
                if s[i]==map[s[j]]:
                    try:
                        ind=s.index(map[s[j]],i+1,j)
                        s=s[i:ind]+s[ind+1:j]+s[j+1:]
                        j=1
                    except ValueError:
                        s=s[i+1:j]+s[j+1:]
                        j=1
                else:
                    j+=2
            except KeyError:
                j+=2
        if len(s)==0:
            return True
        else:
            return False
