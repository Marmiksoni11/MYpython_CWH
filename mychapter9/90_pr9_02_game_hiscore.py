#my try 

# import random
# score =  random.randint(1,15) #prints random number from 1 to 15 
# f = open('hiscore.txt', 'a')
# if score>10:
#     t = f.write(str(score))
#     print(f"u broke the highscore = {score}")
# else:
#     pass
#     print(f"u didnt break the highscore = {score}")
# f.close()



#harry's way (random by me)
import random
n = random.randint(1,50)
def game():
  return n 
score = game()

with open("hiscore.txt","r") as f: #reads the file
    highscorestr = f.read()

if highscorestr == "":#checking for blank
    with open("hiscore.txt","w") as f:#overwrites highscore if score greater
        highscorestr = f.write(str(score))
        print(score, "new higscore !")

elif int(highscorestr) < score:#checking for highscore
    with open("hiscore.txt","w") as f:#overwrites highscore if score greater
        highscorestr = f.write(str(score))
        print(score, "new higscore !")

else: 
    print("not reached the higscore = ", score)