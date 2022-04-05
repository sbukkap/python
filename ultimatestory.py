from sys import exit
print('Greetings warrior! Welcome to the Satan\'s Arena>->')
x=input()

while x != '':
    print('Dont give up warrior!...Figure out the right key to continue!')
    x=input()

print("in case you've forgotten(as most heros do)...you were once a firece unbeaten piece of sh*t")
z=input()

while z!='':
    print('(you know what to do)')
    z=input()

print('''but your legacy has been stolen from you by the dark sorceror
and your children(adopted cuz you lack something you shouldn't) were taken prisoners by his men
''')

def final_fight():

    print('So here you are...in the final 1v1 showdaown...facing the boss')
    j=input()

    while j!='':
        print('bruh')
        break

    print('''The Dark sorcerer has immense power and control over the dark energy
    He also has the ability to regen
    do whatever you think of...to defeat him...but remember ....the light to drive away darkness lies WITHIN you
    ''')
    l=input('''pick your choice(1,2,3)
    1.Face the dark sorcerer with your weapon
    2.Run away
    3.........''')

    if l=='1':
        print('The sorcerer was stronger than you :( Rip ')
        final_fight()
    elif l=='2':
        print('You are unfit for a warrior')
    elif l=='3':
        m=input('What  else would you do? ')
        if 'within' in m:
            print('''You understood the true meaning of power
            You unleashed the hidden power inside you
            You are now stronger than Saitama
            You are Victorious(END)
            Go get your childern btw''')
        else:
            print('You lost to the dark sorceror')

def door1():

    print('''You have a giant one eyed monster eagerly waiting for food(you can see water coming out of his mouth)
His heart is visible and is shining red
You also have a gun in your hand''')
    d=input()
    while d!='':
        print('bruh')
        d=input()
    print('What would you do')
    u=input()
    if 'shoot' in u and 'heart' in u:
        print('You successfully made it through the door')
        final_fight()
    else:
        print('The monster has its tasty Snacc')
        door1()

def door2():

    print('''there is fire everywhere around you and beside you lies a shining lamp
    the fire is closing towards you ''')
    o=input('What would you do?')
    if 'lamp' in o:
        print('You made your way out!')
        final_fight()
    else:
        print('YOu are now tasty,roasted food! ')
        door2()

def door3():

    print('You have a big chocolate cake in front of you..what would you do?')
    p=input()
    if 'eat' in p:
        print('Was the cake good?...you made it to the showdown btw')
        final_fight()
    else:
        print('wait...what?')
        door3()

def chapter_one():

    print('you now have three doors of suffering you can choose.(1,2,or 3)')
    t=input()
    if t=='1':
        door1()
    elif t=='2':
        door2()
    elif t=='3':
        door3()
    else:
        print('Wrong input')
        t=input()

def chapter_begins():

    print('So you have made your choice')
    c=input()
    while c!='':
        print('bruh')
        c=input()
    print('You need equipment/badass weapons to fight the sorceror......(or do you want to fight him barehanded?)')
    print('''pick your choice
    you have three options
    1.Imhotep Pounders
    2.Takeo's great sword
    3.Barehanded''')
    v=input()
    if v=="Imhotep Pounders":
        print('Good choice!the pounders have been created for chaos ....go get that b!tch')
    elif v=='Takeo\'s great sword':
        print('Great!Takeo wouldn\'t like this but.... This sword has been relentless when it comes to killing')
    elif v=='Barehanded':
        print('Get ready to have your a** whooped(difficulty level :insanely impossible) ...go back and pick up one of those')
    else:
        print('Wrong input')
        v=input()
    chapter_one()
y=input('Do you wish to regain your glory ?(yes or no)')

if y=="yes":
    chapter_begins()
elif y=="no":
    print('How can you be such an A**?')
    exit(0)
else:
    print('Wrong input')
    exit(0)

print('THE END BTW')
print(' :) ')
