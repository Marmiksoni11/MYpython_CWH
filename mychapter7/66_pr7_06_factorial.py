# factorial of  a number
# n! = 1x2x3x4x5.....xn
#5! = 1x2x3x4x5 = 120


num = int(input("Enter your number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}") 
    
