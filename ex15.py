from sys import argv
script,filename=argv
x=open(filename,'a+')
x.read()
x.seek(0)

x.append('there')
x.close()
