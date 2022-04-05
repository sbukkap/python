"""
lambda function
it is an anonymous function which takes in arguments in the form lambda <arg1>,<arg2>..<argn>
and then youwrite the function like:
lambda <args>:<func>
what ever you'll be writing as the function using your arguments will be evaluated and returned
also since this func. will be returning a value it must be assignmed to a variable
like
c=lambda <args>:<func>        ---> final form : )
its main use is when you use it iteratively
like for every element of a list you want to perform some operation
then this will come in handy
"""
"""
l=[1,2,3,4,5,6,7]
for i in l:
    r = lambda i:i*i
    print(r(i))
"""
"""
l=['abc','defg','hi']
def func(i):
    return len(i)
l.sort(key=func)
print(l)
"""
l=[[1,2],[0,4],[3,4],[2,3]]
def work(i):
    return i[0]
l.sort(key=work)
print(l)
