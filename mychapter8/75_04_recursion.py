#recursion : function calls itself
# recursion is used when u have a clear formula of  code


# program to print factorial of a number uing recursion
# n! = 1*2*3*4...*n

# n = 4 
# a = 1
# for i in range(n):
#     a = a * (i+1)
# print(a)


# def factorial_iter(n): 
#     a = 1
#     for i in range(n):
#       a = a * (i+1)
#     return a
# f = factorial_iter(5)
# print(f)


# now if n = 5 then 
# n! = 1*2*3*4*5 ...*n
# can also be written as 1*2*3*(n-1)*5 or, 
# n! = (n-1)! *n , this is a formula of n! so,

def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(4)) 

#above factorial_recursive function works as follows 
  
'''factorial (4) #dont know the value of fact4 
   4 x [factorial (3)] likewise dont know 3 niether
   4 x 3 x [factorial (2)]  then 2 niether
   4 x 3 x 2 x [factorial (1)] but 1 was declared as 1'''
   # so, 4x3x2x1 = 24 