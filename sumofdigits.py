print('input integer value')
try:
    x=int(input('>'))
    sum=0
    while x!=0:
        y=int(x%10)
        sum=sum+y
        x=int(x/10)
    print(f'The sum of digits of this number is {sum}')
except:
    print('This number is not an integer')
