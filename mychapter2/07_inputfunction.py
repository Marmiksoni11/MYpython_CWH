# here if we input  number we still get type as "string" thats why we do type casting

import string


a = input ("Enter your name : ")
print (a)
print(type (a))


# TYPECASTING

b = input ("Enter your name2 : ")
# if we take number as an input then we have to convert the string into an INT (if possible, i.e. 1bb2
# cant be converted into a int)
# that can be done by :
b = int(b)
print (b)
print (type(b))
'''here type of a is a string even if the input is a number so we do typecasting'''
'''however this is done only IF IT IS POSSIBLE TO DO.'''

import string 

a = input ("Enter a number: ")
a = int(a)
print (a)
print (type(a))