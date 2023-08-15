# pr 06 frnds and there fav lang

favlang = {} #here favlang is initiallized as empty for future use
#taking input
a = input("Enter your language marmik : ")
b = input("Enter your language krish : ")
c = input("Enter your language kavya : ")
d = input("Enter your language kavya : ")
#here names are the leys and entered values will be values
favlang ["marmik"] = a
favlang ["krish"] = b
favlang ["kavya"] = c
favlang ["mahi"] = d
print (favlang)

#pr 07 what if names of two frnds are same?

favlang ["marmik"] = a
favlang ["krish"] = b
favlang ["kavya"] = c
favlang ["kavya"] = d # considers value from last one which is this
print (favlang)


#pr 08 what if langs are same?

'it doesnt matter is still prints the values. keys have to be unique not values.'
