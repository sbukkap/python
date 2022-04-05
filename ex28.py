class Dryfruits():
    def __init__(self,colour,energy,price):
        self.colour=colour
        self.energy=energy
        self.price=price
        self.email=colour+'.'+energy+'@gmail.com'
    def explainer(self):
        print (f'''this dryfruit is {self.colour} and it has {self.energy} of vitamins and it costs {self.price}
        can u guess it ? :)
         your email btw is {self.email} ''')
    def price_raise(self):
        return self.price*2



kaju=Dryfruits('White','180kCal',840 )
badam=Dryfruits('Brownish','200kCal',720)

badam.explainer()
print(kaju.price_raise())
kaju.explainer()
