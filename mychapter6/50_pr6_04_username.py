# check wheather the username contains less then 10 characters or not
#my way
username = input("Enter your Username: ")
if (len(username)>10):
    print("Greater than ten chars")
elif(len(username)<10):
    print("less than ten chars")
else:
    print("ten chars")


