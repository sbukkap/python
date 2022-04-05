from sys import argv
script,fromfile,tofile=argv
x=open(fromfile,'r')
y=open(tofile,'w')
z=x.read()
y.write(z)
print("Dne :)")
x.close()
y.close()
