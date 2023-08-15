# pr 03 prevent print() to print in a new line 
# 
# like here 
print("hello") 
print("how")# prints in a new line 
print("are")# prints in  a new line 
print("you")# prints in  a new line 

#it will print 
#hello 
#how 
#are
#you

#but the question asks to prevent the above printing style

#every time the built in functions print it prints /n (escape seq) at the end as a defualt argument 
# so in order to prevent this we use end=""
# end= removes the extra spaces and cancels /n escape seq
print("hello", end=" ") 
print("how", end=" ")
print("are", end=" ")
print("you", end=" ")
#prints hello how are you