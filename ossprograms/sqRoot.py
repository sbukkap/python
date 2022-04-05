#sqare root by newtons method
print('''This is the Newton-Raphson's Method of finding square root of a given number
Enter a number u want to find root for''')
c=int(input())
x=c
for i in range(1,x+1):
    x=(x+(c/x))/2
print(f'The square root of {c} is {x}')
