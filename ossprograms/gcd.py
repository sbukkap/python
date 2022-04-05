print('input the numbers u want to find gcd for')
x=int(input())
y=int(input())
gcd=0
for i in range(1,(max(x,y))+1):
    if x%i==0 and y%i==0:
        gcd=i
print(f"The GCD of {x} and {y} is {gcd}")
