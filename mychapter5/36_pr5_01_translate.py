# my way maarwadi to english, and hindi to english  translation using dicts
# and also giving them options
 

tmarwadi = {
    "kaalo" : "stupid",
    "leeko" : "used for talking about a person secretly in front of him",
    "khomo" : "the guy's listening. / he will be sus",
    "montois ni" : "he dont listen(or not getting convinced)"
}

thindi = {
    "pankhaa" : "fan",
    "paagal" : "stupid",
    "aadmi" : "man",
    "aurat" : "woman"
}

print(tmarwadi["khomo"])
print(thindi["pankhaa"])

# print(tmarwadi)
# print(thindi)


#for printing marwadi words
'''print("Options are : ", tmarwadi.keys())
a = input ("Enter your marwadi word :  ")
print("the meaning of your marwadi word is :  ", tmarwadi[a])'''

#for printing hindi words
'''print("Options are : ", thindi.keys())
b = input ("Enter your hindi word :  ")
print("the meaning of your hindi word is :  ", thindi[b])''' 


#however a good coder always avoid showcasing errors so we use .get instead 
# of normal way, so it returns none if key isnt present in the options

#for printing marwadi words

print("Options are : ", tmarwadi.keys())
a = input ("Enter your marwadi word :  ")
print("the meaning of your marwadi word is :  ", tmarwadi.get(a)) 

#for printing hindi words
print("Options are : ", thindi.keys())
b = input ("Enter your hindi word :  ")
print("the meaning of your hindi word is :  ", thindi.get(b))