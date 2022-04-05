class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.lstrip()
        final_string=''
        if not str:
            return 0

        if str[0]=='+':
            final_string+=str[0]
            str=str.replace('str[0]','')
        elif str[0]=='-':
            final_string+=str[0]
            str=str.replace('str[0]','')
        else:
            pass
        for i in range(len(str)):
            if str[i] in '0123456789':
                final_string+=str[i]
            else:
                break
        if final_string=='+' or final_string=='-':
            return 0
        elif final_string=='':
            return 0
        else:
            if int(final_string)>2**31 - 1:
                return 2**31 - 1
            elif int(final_string)<-2**31:
                return -2**31
            else:
                return int(final_string)








        
