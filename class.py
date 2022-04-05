class Shreekar:
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight
    def sayname(self,name,section):
        print(f'my name is {name} and im from {section}')
    def attendance(self,days,classes):
        print(f'my attendance is {days*classes}')
    def descript(self):
        print(f'im {self.height} tall and weigh about {self.weight}')
    def sum(self,a,b):
        print(f'the sum is {a+b}')
class shr1(Shreekar):
    def arrogant(self,answer):
        if answer == 'yes':
            print('FO')
        else:
            print('Good Boi')
    def xyz(self):
        print(f'hey there {self.height}')
class shr2(Shreekar):
    pass
"""
obj1=Shreekar('6ft4','85kilo')
obj1.sayname('Shreekar','AZXDWQ')
obj1.descript()
obj2=Shreekar('6ft1','87kilo')
obj2.sayname('Shredder','AZWQDWQ')
obj2.descript()
obj3=shr1('3ft1','33kilo')
obj3.descript()
obj3.arrogant('no')
"""

obj3.xyz()
"""
obj3.sum(3,4)
obj1.sum(3,4)
"""
"""
obj4 = shr2('ss','ff')
obj4.attendance(5,6)
print(isinstance(obj3,shr2))
"""
