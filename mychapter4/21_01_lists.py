#LISTS

#Create a list using []

a = [1,2,3,56,6,7]
#access using indices , and change by asssiging changed value in index 
a[0]=22
print(a)
print(a[0])
print(a[2])


'''as seen below strings cant be changed, or we cant assign values like in lists'''
# a = "my name is marmik"
# a[10] = 90


# we can create a list with different types of items
b = [1, "marmik", False, 34.5]#--> here there's int , str, bool, and float
b[2] = True #changing of value in a list is posible  
print(b)
print(b[0:3]) #slicing the list
print(b[-4:-1])
