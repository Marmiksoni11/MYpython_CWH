# STRING FUNCTIONS
# LENGTH

intro = "my name is marmik and i am a student" 
print(len(intro)) #shows full length of characters counting from 1.
print (intro.endswith("a"))
print(intro.startswith("name"))
print(intro.count("i")) # count number of given valur in the input,like i is three times
print (intro.capitalize()) # capitalizes first letter 
print(intro.find("marmik")) # it finds the word and shows the first 
#index of firstoccurence the found word like in "marmik" the 
# words first letter m is at the 11th index so it shows 11

print(intro.replace("marmik","Marmik soni")) # replaces words and characters


this = "     marmik is good      "
print(this)
print(this.strip()) 
#removes extra white spaces from only either sides