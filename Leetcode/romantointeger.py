class Solution:
    def romanToInt(self, s: str) -> int:
        mydict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        x=0
        i=0
        while i<=len(s)-2:
            if mydict[s[i]]<mydict[s[i+1]]:
                x+=(mydict[s[i+1]]-mydict[s[i]])
                i+=2
            else:
                x+=mydict[s[i]]
                i+=1
        if len(s)==1:
            return mydict[s[0]]
        elif mydict[s[-1]]<mydict[s[-2]] or mydict[s[-1]]==mydict[s[-2]]:
            x+=mydict[s[-1]]
        return x




            
