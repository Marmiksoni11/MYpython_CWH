# Rock Paper Scissors
#practicing program by myslef

import random

def gamewin(comp,you):
    if comp == you:
        return None
    #checking for rock
    if comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
             return True
    if comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
             return True
    if comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
             return True

        

print("Comp Turn : Choose , Rock(r),Paper(p) or Scissors(s)?: ")

randno = random.randint(1,3)
if  randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("Your turn: Choose , Rock(r),Paper(p) or Scissors(s)?: ")
a = gamewin(comp,you)

print(f"Computer Chose, {comp}")
print(f"You Chose, {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("You Win!")
else :
    print("You Lose!")