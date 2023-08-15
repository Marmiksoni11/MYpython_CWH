#1 




#i was trying to replace list to string thats why so many trial and failure

# s = input("Enter your sentence: ")
# vowels = ["a","e","i","o","u"]
# for i in vowels:
#     if i in s:
#         print(s.replace(vowels[i]),"*")
#     else:
#         print(s)
            
  


# post = input("Enter your post: ")
# p = post.lower() #coverts string to lowercase
# h = ("harry") 
# if h in p : #compares lowercase string with h i.e. harry
#     print("It is talking about harry")
# else:
#     print("It isn't talking about harry")


s = input("enter string: ")
print(s)#shows entered string
for i in s: #prints each letter 
    if i in 'AEIUOaeiou': #checks if each letter is a 'AEIOUaeiou'/vowel or not
        print("*",end='') # if true print "*"
    else:
        print(i,end='') # if false print the letter




    
