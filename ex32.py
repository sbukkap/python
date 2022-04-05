class employee():
    incr_in_pay=1.04
    def __init__(self,salary):
        self.salary=salary
    @classmethod
    def sforclass(cls,amount):
        cls.incr_in_pay=amount

class Dev(employee):
     def __init__(self,salary,age):
         super().__init__(salary)
         self.age=age
     def hi(self,Name):
         print(f'So this guy that you just named....{Name} earns{self.salary} and is {self.age}old!')
     def __repr__(self):
         return 'this is a class'
     def __str__(self):
         return 'this is gonna get printed instead of repr return string'
o1=Dev(220000,230
o2=Dev(330000,25)
#o1.hi('Shreekar')
print(o1)
print(Dev)
