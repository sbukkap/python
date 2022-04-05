print('Enter the range of prime numbers(ex. if you want to find out prime numbers between 1 to 50,enter 50)')
x=int(input())

for i in range(1,x+1):
    noofdivisors=0
    for y in range(1,i+1):
        if i%y==0:
            noofdivisors+=1
    if noofdivisors==2:
        y=1
        print(i)
    else:
        y=1
        continue
