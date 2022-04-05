from sys import argv
x,textfilename=argv
print(f"your file name is{textfilename}")
y=open(textfilename)
print(y.read())
