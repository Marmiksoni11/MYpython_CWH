# problem 04 len of following very imp 

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)


# In a set 20.0 is not considered as a float but int
# 20.1 is considered as a float

s.add(20.1)
print(s)
print(len(s))

# problem 05 

s = {} #empty dict
print(s)

s = set() #empty set
print(s)