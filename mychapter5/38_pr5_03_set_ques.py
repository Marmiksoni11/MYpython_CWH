# can we have 18 int and 18 as a str in  aa set as values

a = {18,"18"}
print (a)
print(type(a))
print(len(a))

# Yes we can and both will print as they are not sam acc to python
# if they were both repetative as only int or only string then
#18 prints only once

b = {18,18}
print(b) #prints once 18 

c = {"12","12"}
print(c) #print once 12