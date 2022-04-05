from sys import argv
scriptname,x=argv
if '+' in x:
    y=x.split('+')
    print(f'The sum of {y[0]} and {y[1]} is {int(y[0])+int(y[1])}')
elif '-' in x:
    y=x.split('-')
    print(f'The difference of {y[0]} and {y[1]} is {int(y[0])-int(y[1])}')
elif '*' in x:
    y=x.split('*')
    print(f'The product of {y[0]} and {y[1]} is {float(y[0])*float(y[1])}')
elif '/' in x:
    y=x.split('/')
    print(f'The quotient of {y[0]} and {y[1]} is {float(y[0])/float(y[1])}')
elif '%' in x:
    y=x.split('%')
    print(f'The modula of {y[0]} and {y[1]} is {float(y[0])%float(y[1])}')
else:
    print('Enter a valid operator')
