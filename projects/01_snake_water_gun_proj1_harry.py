


import random # this is the random module

# snake water gun or Rock Paper Scissors 
def gamewin(comp,you):
    if comp == you: # if both a equal declare tie
        return None #for tie 

#checking  all posibilities when comp choose snake(s)
    if comp == 's':
       if you == 'w':
        return False 
       elif you == 'g':
          return True 

#checking  all posibilities when comp choose water(w)  
    if comp == 'w':
       if you == 'g':
        return False 
       elif you == 's':
          return True 

#checking  all posibilities when comp choose gun(g)
    if comp == 'g':
       if you == 's':
        return False 
       elif you == 'w':
          return True 
    
randno = random.randint(1,3) #this is the randint function which genearates a
# random number from the given range
print(randno)


print("Comp turn : Snake(s) Water(w) or Gun(g)?")

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("Your turn : Snake(s) Water(w) or Gun(g)? : ")

a = gamewin(comp,you)# calling gamewin function

#showing computer's, and your choises after input
print(f"Computer chose  {comp}  ")
print(f"You chose  {you}  ")

if a == None: #for tie
    print ("The game is a tie!")
elif a: # if a is true then u win
    print("You Win!")
else: # if a is false u loose
    print("You Lose!")