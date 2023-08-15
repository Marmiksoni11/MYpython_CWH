# # while loop 
# i = 0
# while i<10:
#     print("yes " + str(i))
#     #above loop without below lines is an infinite loop
#     i = i+1
# print("done")


#quick quiz

# a = 1 
# while a<51:
#     print(a) 
#     a = a+1

#above loop means start from a , if a<51 than print a(the number) 
# then increase the number by 1 a = a+1
# the loops keeps going until 51<51, which is false

'''now the below loop'''

# a = 1 
# while a<51:
#     a = a+1
#     print(a) 
# this loop means start with 1, if a<51,true then a =a+1, i.e. 2
# print(a) then 2 will be printed 
# then till 50<51,true, a=a+1, i.e. 51 is printed
# so it prints from 2 to 51


# i = 0 #starts from 0 till 4 i.e. total 5 times 
# while i<5:
#     print("Harry")
#     i = i+1


#quickquiz content of a list

# a = [1,2,3,4,5,6]
# i = 0 #index 0 
# while i < len(a):#loops till 5th index as 6th is the total len
#     print(a[i]) #prints the number at index i 
#     i = i + 1 #increase 1 and loop again


# fruits = ["watermelon","banana","apple","orange","melon"]
# i = 0 #index 0 
# while i < len(fruits):#loops till 5th index as 6th is the total len
#     print(fruits[i]) #prints the fruit at the given index in i
#     i = i + 1 #increase 1 and loop again


a = [16,256,13,24,35,46]
i = 0 #index 0 
while i < len(a):#loops till 5th index as 6th is the total len
    print(a[i]) #prints the number at index i 
    i = i + 1