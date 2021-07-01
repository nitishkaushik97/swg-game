import random

def game(c,y):
    if c==y:
        return None
    elif c=='snake':
        if y=='water':
            return False
        elif y=='gun':
            return True
    elif c=='water':
        if y=='gun':
            return False
        elif y=='snake':
            return True
    elif c=='gun':
        if y=='snake':
            return False
        elif y=='water':
            return True

n=random.randint(1,3)
if n==1:
    comp='snake'
elif n==2:
    comp='water'
elif n==3:
    comp='gun'


x=raw_input("Your Turn, Type:\n  s for 'Snake' w for 'Water' g for 'Gun' ")
if x=='s':
    you=str('snake')
elif x=='w':
    you=str('water')
elif x=='g':
    you=str('gun')
else:
    print"Oops! Wrong entry"
a=game(comp,you)


print("You chose"),you
print("Bot chose"),comp

if a==None:
    print("It's a tie.")
elif a:
    print"You Win!"
else:
    print"You Lose!"
