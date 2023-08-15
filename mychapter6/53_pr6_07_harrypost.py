#given post is talking about harry or not
#here we need to check for both lowercase and uppercase characters




#program before
post = input("Enter your post: ")
h = ["harry","Harry","HaRrY","HARRY"] #creating a list is a waste of time as 
# you cant add all possible combinations of a word by yourself in the list, 
# as we want a case sensitive program 
if h in post :
    print("It is talking about harry")
else:
    print("It isn't talking about harry")



#program incomplete(yesterday, but then i found .lower() method, myself)
# here .lower converts any string irresptive if its case to lowercase
# so it can catch every ty pe "Harry,HaRrY,haRRY..etc"


#program after
post = input("Enter your post: ")
p = post.lower() #coverts string to lowercase
h = ("harry") 
if h in p : #compares lowercase string with h i.e. harry
    print("It is talking about harry")
else:
    print("It isn't talking about harry")




'''below were experiments'''
# if ("h" in post):
#     harry = True
# elif ("a" in post):
#     harry = True
# elif ("r" in post):
#     harry = True
# elif ("y" in post):
#     harry = True
# elif ("H" in post):
#    harry = True
# elif ("A" in post):
#    harry = True
# elif ("R" in post):
#    harry = True
# elif ("Y" in post):
#    harry = True

# else:
#     harry = False

# if harry:
#     print("talking")
# else :
#     print("not talking")

