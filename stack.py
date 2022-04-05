
class stack():
    def __init__(self):
        self.s=[]
    def isEmpty(self):
        return self.s==[]
    def Topelement(self):
        if len(self.s)==0:
            print('empty')
        else:
            return self.s[-1]
    def popp(self):
        if len(self.s)==0:
            print('empty')
        else:
            return self.s.pop()
    def add(self):
        x=input('enter element ')
        self.s.append(x)

o=stack()
o.add()
