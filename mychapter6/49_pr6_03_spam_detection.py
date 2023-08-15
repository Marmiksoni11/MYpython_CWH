#spam detection

#my way
comment = input("Enter a comment: ")
if ("make a lot of money" in comment):
    print("Spammer Detected !")
elif ( "buy now" in comment):
    print("Spammer Detected !")
elif ( "click this" in comment):
    print("Spammer Detected !")
elif ( "subscribe this" in comment):
    print("Spammer Detected !")
else:
    print(comment)
 

 
 
#harrys way
text = input("Enter the text\n")

if("make a lot of money"):
    spam = True 
elif ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
else:
    spam = False

if (spam) :
    print("this text is spam")
else:
    print("this is not a spam text")    