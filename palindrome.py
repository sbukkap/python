print('Enter your number')
x=input()
def even_case(count):
    f=0
    l=count-1
    while(f<l):
        if x[int(f)]==x[int(l)]:
            f+=1
            l-=1
        else:
            print('Not a palindrome')
            break
    if x[int(f)]==x[int(l)]:
        print('The number is a palindrome')
def odd_case(count):
    f=0
    l=count-1
    while(f!=l):
        if x[int(f)]==x[int(l)]:
            f+=1
            l-=1
        else:
            print('Not a palindrome')
            break
    if x[int(f)]==x[int(l)]:
        print('The number is a palindrome')
count=len(x)
if count%2==0 :
    even_case(count)
else :
    odd_case(count)
