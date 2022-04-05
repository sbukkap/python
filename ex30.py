class employee():
    incr_in_pay=1.04
    def __init__(self,salary):
        self.salary=salary
    @classmethod
    def sforclass(cls,amount):
        cls.incr_in_pay=amount

obj1=employee(200000)
obj2=employee(250000)
obj2.incr_in_pay=1.06

print(employee.incr_in_pay)
print(obj1.incr_in_pay)
print(obj2.incr_in_pay)
employee.sforclass(1.07)
print(employee.incr_in_pay)
print(obj1.incr_in_pay)
print(obj2.incr_in_pay)
