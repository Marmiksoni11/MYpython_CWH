

#my way 
# def greatest(num1,num2,num3):
    
#   if(num1>num3):
#       f1 = num1
#   else:
#       f1 = num3
  
#   if(num1>num2):
#       f2 = num1
#   else:
#       f2 = num2
  
#   if(f1>f2):
#     return f1
#   else: 
#     return f2
# print(greatest(12,33,65))


#harrys ways 
def maximum(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1 
        else:
            return num3 
    else:
        if (num2>num3):
          return num2
        else:
          return num3


print(maximum(22,33,44),"is the greatest")


