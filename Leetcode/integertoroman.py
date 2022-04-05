class Solution:
    def intToRoman(self, num: int) -> str:
        if 1 <= num <= 3999:
            roman={1:'I',2:'II',3:'III',4:'IV',40:'XL',400:'CD',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',90:'XC',900:'CM',10:'X',50:'L',100:'C',500:'D',1000:'M'}
            roman_list=[]
            i=0
            final=''
            r=num%10
            if num<10:
                roman_list.append(num)
            else:
                while 10<num:
                    r=num%10
                    roman_list.append(r*(10**i))
                    num=num//10
                    i+=1
                roman_list.append(num*(10**i))
                roman_list.reverse()
            for i in range(len(roman_list)):
                if roman_list[i] in roman:
                    final+=str(roman[roman_list[i]])
                else:
                    s=str(roman_list[i])
                    if s[0] in '23':
                        if '000' in s:
                            final=final+(int(s[0])*'M')
                        elif '00' in s:
                            final+=(int(s[0])*'C')
                        elif '0' in s:
                            final+=(int(s[0])*'X')
                        else:
                            pass
                    else:
                        if '00' in s:
                            final+=('D'+((int(s[0])-5)*'C'))
                        elif '0' in s:
                            final+=('L'+((int(s[0])-5)*'X'))
            return final
        else:
            return 0
print()
