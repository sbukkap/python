"""
 from a given string,using sliding window approach ,find the longest substring with k distinct characters
"""
def longest_substr(l,k):
    windowStart=0
    longest_substring_length=-10000
    map={}
    length_tracker=0
    for windowEnd in range(len(l)):
        if l[windowEnd] in map:
            map[l[windowEnd]]+=1
        else:
            map[l[windowEnd]]=1
        while len(map)>k:
            map[l[windowStart]]-=1
            if map[l[windowStart]]==0:
                map.pop(l[windowStart])
            windowStart+=1
        longest_substring_length=max(longest_substring_length,windowEnd-windowStart+1)
    return longest_substring_length
