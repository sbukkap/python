x=input('enter file name')
f=open(f'C:\\Users\\iamop\\OneDrive\\Desktop\\{x}','r')
s=f.read()
maxwordcount=0
str=s.lower().replace(',','').replace('.','').replace('\n','').split(" ")
print(str)

for i in range(len(str)):
    wordcount=1
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            wordcount+=1
    if wordcount>maxwordcount:
        mostrepword=str[j]
        maxwordcount=wordcount

print(f'the most repeated word is {mostrepword} and its count is {maxwordcount}')
