#relational operators
#<=
#>=
#==


#logical operators

#and operator, both condtions must be true

age = 21
if (age>17 and age<20):
    print(True)
else:
    print(False)


# or operator, either this or that must be satified for condtion to be true 

age = 21
if (age>17 or age<20): #here it is true as 21>17
    print(True)
else:
    print(False)


# not operator, inverse of true and false

age = 21
if not (age>17): #prints false as condition here is 21>17 satisfied
    print(True)
else:
    print(False)


