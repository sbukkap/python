from sys import argv
script,filename=argv
x=open(filename,'r')
print(x.readline(),end='')
print(x.readline())
