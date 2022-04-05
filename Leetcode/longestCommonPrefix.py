class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        first_element=strs[0]
        felem_len=len(first_element)
        for i in strs[1:]:
            while first_element != i[:felem_len]:
                first_element=first_element[:(felem_len-1)]
                felem_len-=1
            if felem_len==0:
                return ''
        return first_element
                    
