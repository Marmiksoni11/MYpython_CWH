#basic calculator by myself 


#asking which operation to perform


cal = input("add(+), subs(-), mul(*), div(/), Enter the Operation you want to perform: ")
print(f"you chose {cal}")


#making the addition function to do sum of given elements
def addition(l):
    return sum(l)  

'likewise'

#substraction function
def substraction(x,y):
    return x-y  

#multiplication function
mul = 1
def multi(mul):
    for i in range(len(l1)):
        mul = mul*l1[i]
    return mul


#division function
def division(x,y):
    return x/y 



#checking for every operator +-*/
if cal == "+":
    #taking a list input for multiple elements to add
    l = []
    n = int(input("Enter the number of elements : "))
    for i in range(0,n):
     elements = int(input("Enter the elements :  "))
     l.append(elements)
     print(l)

     a = addition(l)#calling the function
     print("The sum of the given elements = ", int(a))



elif cal == "-":
     #taking input of two numbers x,y
     x = int(input("Enter your first element: "))
     print(x) 
     y = int(input("Enter your second element: "))
     print(y)
     
     b = substraction(x,y)#calling the function
     print("The diffrence of the given elements = ", b)


elif cal == "*":
    #taking a list input for multiple elements to multiply
     l1 = []
     num = int(input("Enter the number of elements : "))
     for i in range(0,num):
        elements1 = int(input("Enter the elements :  "))
        l1.append(elements1)
        print(l1)
        
        c  = multi(mul)#calling function
        print(f"the product of given elements = {c}")



elif cal == "/":
    #taking input of two numbers x,y
     x = int(input("Enter your first element: "))
     print(x) 
     y = int(input("Enter your second element: "))
     print(y)
     
     d = division(x,y)#calling the function
     print("The division of the given elements = ", d)

else:
    print("invalid input")



# mul = 1
# def multi(mul):
#     for i in range(len(l)):
#         mul = mul*l[i]
#     return mul
# l = []
# n = int(input("Enter the number of elements : "))
# for i in range(0,n):
#     elements = int(input("Enter the elements :  "))
#     l.append(elements)
#     print(l)

    
# a  = multi(mul)
# print(a)












