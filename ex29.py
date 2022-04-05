class Employee():
    increment=1.12
    no_of_employees=0
    def __init__(self,salary):
        self.salary=salary
        Employee.no_of_employees+=1
    def raise_salary(self):
        print(f'The new salary is {self.salary*self.increment}')



object1=Employee(50000)
object2=Employee(75000)
object1.increment=2.12
object1.raise_salary()
print(Employee.no_of_employees)
