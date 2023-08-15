#multiplication table using for loop 

#my ways
#table with and without

 #without format
num = int(input("Enter your Number: "))
for item in range(1,11):
    print(num*item)

#with format
num = int(input("Enter your Number: "))
for item in range(1,11):
     print(num , "*" , item  ,"=" , (num*item))


#harrys way (best way)
num = int(input("Enter your number: "))
for i in range(1,11):
    print(str(num) + "X" + str(i) + "=" + str(num*i))
    # so if you want to do typecasting inside print then u need to use a plus to join
    # it with a string and not coma.




#multiplication table  using while loop
num = int(input("Enter your number: "))
i = 1 
while i<11:
    print(num*i) 
    i = i + 1   


# multiplication table using while loop with original format 
# prints "2 * 2 = 4" 
num = int(input("Enter your number: "))
i = 1 
while i<11:
    print(num , "*" , i  ,"=" , (num*i)) 
    i = i + 1   

# i = 10
# print("marmik",i) #prints marmik 10 

