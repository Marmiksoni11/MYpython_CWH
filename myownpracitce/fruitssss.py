# fruits = []
# # n = int(input()) 
# for i in range(1,8):
#     b = input(f"Enter the fruit {i}: ")
#     fruits.append(b)
    

# print(fruits)





# a1 = input ("Enter fruit no. 1 :")
# a2 = input ("Enter fruit no. 2 :")
# a3 = input ("Enter fruit no. 3 :")
# a4 = input ("Enter fruit no. 4 :")
# a5 = input ("Enter fruit no. 5 :")
# a6 = input ("Enter fruit no. 6 :")
# a7 = input ("Enter fruit no. 7 :")

# fruits = [a1,a2,a3,a4,a5,a6,a7]
# print(fruits)

lst = []
for i in range(1,7):
    marks = int(input(f"enter marks of student {i}: "))
    lst.append(marks)

lst.sort()
print(lst)