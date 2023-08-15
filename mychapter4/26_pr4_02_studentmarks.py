#accept marks of 6 students and display them in a sorted manner

# my way
 
# a1 = input("Enter marks of student 1: ")
# a2 = input("Enter marks of student 2: ")
# a3 = input("Enter marks of student 3: ")
# a4 = input("Enter marks of student 4: ")
# a5 = input("Enter marks of student 5: ")
# a6 = input("Enter marks of student 6: ")
# #bcoz of str input numbers are in str so typecast them,
# a1 = int(a1) 
# a2 = int(a2)
# a3 = int(a3) 
# a4 = int(a4) 
# a5 = int(a5) 
# a6 = int(a6) 
# print(type(a1))
# print(type(a2))
# print(type(a3))
# print(type(a4))
# print(type(a5))
# print(type(a6))
# l = [a1,a2,a3,a4,a5,a6]
# l.sort()
# print(l)


#  harry way 

a1 = int(input("Enter marks of student 1: "))
a2 = int(input("Enter marks of student 2: "))
a3 = int(input("Enter marks of student 3: "))
a4 = int(input("Enter marks of student 4: "))
a5 = int(input("Enter marks of student 5: "))
a6 = int(input("Enter marks of student 6: "))
#to check type cast
print(type(a1))
l = [a1,a2,a3,a4,a5,a6]
l.sort()
print(l)