x=int(input('enter the number'))
first_elem=0
next_elem=1
sum=0
while first_elem<=x:
    sum=first_elem+next_elem
    print(first_elem)
    temp=next_elem
    next_elem=sum
    first_elem=temp
