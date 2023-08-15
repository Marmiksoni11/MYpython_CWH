
# example of function 

cel = int(input("Enter the celsius temp: "))
def far(cel):
    return (cel * (9/5))+32
temp = far(cel)

print(str(cel) + " degrees celsius is " + str(temp)+" degrees farenheit")

'''in above program :

def far(cel): 
    return (cel * (9/5))+32   # here we write (cel..) and not far(cel..)
temp = far(cel)
'''

#if we write far(cel) it becomes recursive 
'''like below'''

cel = int(input("Enter the celsius temp: "))
def far(cel):
    return far(cel * (9/5))+32 # prints "previous line repeated 996 more times"
temp = far(cel)

print(str(cel) + " degrees celsius is " + str(temp)+" degrees farenheit")





# example of recurrsion
n = int(input("Enter the value of n: "))
def natural(n):
    if n==0:# this will make the loop to stop when it hits 0
      return 0
    return natural(n-1) + n #here we use natural(..) in order to use reccursion
    
s = natural(n)
print(s)
