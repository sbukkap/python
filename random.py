
import random
s=[1,'a',2,3,4,5,'asdsad']
print(random.choice(s))
random.seed(3)
print(random.choice(s))
random.seed(56)
print(random.choice(s))
print(random.choice(s))
list=[1,2,3,4,5,6,7,8,90]
print(random.shuffle(list))
print(random.uniform(list[2],list[3]))
print(random.uniform(list[2],list[3]))
print(random.random())

