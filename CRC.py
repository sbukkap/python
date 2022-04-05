def xor(s1,s2):
    res = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res+='0'
        else:
            res+='1'
    return res[1:]

f = input('enter frame')

d = input('enter divisor')

mod_f = f+'0'*(len(d)-1)

slice = mod_f[:len(d)]
r = xor(slice,d)
for i in range(len(d),len(mod_f)):
    slice = r + mod_f[i]

    r = xor(slice,d) if slice[0] == '1' else xor(slice,'0'*len(d)
    
print(f'the {len(d)-1} bit redundant code is {r}')
print(f'the frame to be sent to the destination is {f+r}')
