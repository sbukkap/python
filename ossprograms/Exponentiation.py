print('ENter a number')
x=int(input())
print('Enter the power of this number you want to calculate')
y=int(input())
product=1

for i in range(1,y+1):
    product=x*product

print(f'The result is {product}')
