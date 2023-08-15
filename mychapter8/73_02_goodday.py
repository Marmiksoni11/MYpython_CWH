# #quick quiz greet a person    

# #my way, nut with input
# def greet():
#    b = "Good day!"
#    return b 

# name  = input("Enter your name: ")
# a = greet()
# print(a,name)
 

# #harrys way original way

# def greet(name): # def  defines the function greet where container 'name' is defined
#     print("Good day!, "+name)
# #you can call a function n number of times inside the program
# greet("marmik")
# greet("krish")
# greet("kavya")


# there are two types of functions 
# built in functions: len(), print(), range()
# user defined funsctions like 'greet()' in previous code
# you can give your function multiple values like
# in greet(name) 'name' is  one value
# also two or more values can be assigned in function like below
def mysum(sum1,sum2):
    print(sum1+sum2)
mysum(10,11) 

#also can be done by
def mysum(sum1,sum2):
    return sum1+sum2
s = mysum(1,5)
print(s)

