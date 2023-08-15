
print ("The value of 3+1 is",3+1)

# ARITHMETIC OPERATORS

a = 3
b = 1
print ("The value of 3+1 is",3+1)
print ("The value of 3-1 is",3-1)
print ("The value of 3*1 is",3*1)
print ("The value of 3/1 is",3/1)

# what if you print a+b etc ?
print ("The value of 3+1 is",a+b)
'''it gives the same output as above'''

# ASSINGMENT OPERATORS
 
# Add
c = 2
c +=2 
print("The value of is", c)
#subs
d = 5
d -= 3
print("The value of is", d)

#  likewise * / are done 

# what if done altogether?
e=56
e += 2
e -= 5
e *= 5
e /= 6
print (e)
'''it does everything step by step in chronological order +,-,*,/'''

# COMPARISION OPERATORS (they return a boolean i.e. t or f)

f = (2<10)
print(f)

g = (20<=10)
print (g)

h = (2==2)
print(h)

'''not equal to -> != '''
i = (14!=7)
print(i)

# LOGICAL OPERATORS (BOOLEANS BUT WITH LOGIC)

# rules of "and" ,"r" and "not"

#  1. "and" means both must be true, then it says true
bool1 = True 
bool2 = False
bool3 = True  

print ("The value of bool1 and bool2 is", (bool1 and bool2)) 
# here both are not true so it says false.
# but if both are true then true like below.
print ("The value of bool1 and bool3 is", (bool1 and bool3))

# 2. "or" means anyone one should be true, the it will say true
print ("The value of bool1 or bool2 is", (bool1 or bool2))

#3. "not" means inverse, when its f it says t, and vice-versa
print ("The value of not bool2 is", (not bool2))


