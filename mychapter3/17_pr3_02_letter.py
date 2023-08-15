# #my way 

# name = input("Enter your name: ") 
# print("Dear "+ name + " you are selected ! \n18\\09\\2022" )

#acc to ques 

letter = '''Dear <|NAME|>,
greetings from ABC coding house you have been selected !
have a great day ahead!
Date: <|DATE|> '''

name1 = input("Enter your name: ")
date = input("Enter Date: ")
letter = letter.replace("<|NAME|>", name1.capitalize())
letter = letter.replace("<|DATE|>", date)
print(letter)