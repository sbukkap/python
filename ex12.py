from sys import argv
script,filename=argv
x=open(filename,'a')
x.seek(0)
x.write("NooB")
print("FOND")
