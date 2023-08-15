#greatest of 4 numbers


# my way 

a1 = int(input("Enter 1st number : "))
a2 = int(input("Enter 2th number : "))
a3 = int(input("Enter 3th number : "))
a4 = int(input("Enter 4th number : "))
if(a1>a2 and a1>a3 and a1>a4):
    print("first is the greatest of all four")  
elif(a2>a1 and a2>a3 and a2>a4):
    print("first is the greatest of all four")  
elif(a3>a1 and a3>a2 and a3>a4):
    print("third is the greatest of all four")  
else:
    print("fourth is the greatest of all four")  


# harry's way (allows us to print "12 is the greatest")
'''cricket match pattern semifinals b/w 1 vs 4 and 2 vs 3 then b/w top 2 gives final
or the greatest'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is the greatest")#have to conevert f values from int to str to print
else:
    print(str(f2) + " is the greatest")
