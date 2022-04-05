from sys import argv
filename,file2=argv
f=open(f'C:\\Users\\iamop\\OneDrive\\Desktop\\{file2}','r')
count=0
s=f.read()
for i in s:
    if i==' ':
        count+=1
print(f'word count is {count+1}')
