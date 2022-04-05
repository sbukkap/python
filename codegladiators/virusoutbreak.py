def subsequence(virus,case):
    m=len(virus)
    n=len(case)
    i=0
    j=0
    while i<m and j<n:
        if virus[i] == case[j]:
            j+=1
        i+=1
    return j == n
virus=input()
num=int(input())
for i in range(num):
    case=input()
    if subsequence(virus,case):
        print('POSITIVE')
    else:
        print('NEGATIVE')
