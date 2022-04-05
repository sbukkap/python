class ClassLOL:

    def __init__(self,name,subj):

        self.name=name
        self.subj=subj

    def introduce_self(self):

        print(f'Hey my name is {self.name} and im designed to teach {self.subj} ')
#o1=ClassLOL()
#o1.name='Bruv'
#o1.subj='math'
#o2=ClassLOL()
#o2.name="tim"
#o2.subj='Nothing'
#o1.introduce_self()
#o2.introduce_self()
object1=ClassLOL('Not defined','Shit') #instantiating or creating object called object1
object1.introduce_self()#using that object to run the code in class called ClassLOL
