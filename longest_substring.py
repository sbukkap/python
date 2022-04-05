def lengthOfLongestSubstring(s):

        x=''
        max_length=0

        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in x:
                    if len(x)>max_length:
                        max_length=len(x)
                    x=''
                else:
                    x=x+f'{s[j]}'
                    continue
        return max_length

print(lengthOfLongestSubstring('abcabcbb'))
