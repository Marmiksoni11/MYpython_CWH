#user input 8 numbers and print all the unique numbers once
#bcoz it says unique its a set 

a1 = input("Enter your 1st number : ")
a2 = input("Enter your 2nd number : ")
a3 = input("Enter your 3rd number : ")
a4 = input("Enter your 4th number : ")
a5 = input("Enter your 5th number : ")
a6 = input("Enter your 6th number : ")
a7 = input("Enter your 7th number : ")
a8 = input("Enter your 8th number : ")

#typecast to convert string to num

a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
a5 = int(a5)
a6 = int(a6)
a7 = int(a7)
a8 = int(a8)

print(type(a1)) #check typecasting

#convert in set
b = {a1,a2,a3,a4,a5,a6,a7,a8}
print(b)
print(type(b))