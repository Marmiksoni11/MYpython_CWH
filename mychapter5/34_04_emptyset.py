#empty sets

a ={} 
print(a)
print(type(a))#shows dict
#above isnt an empty set 

#an empty set syntax is below
b = set()
print(b)
print(type(b))

#adding values to an empty set

b.add(1)
b.add(2)
b.add(3)
b.add(8)
b.add(6) 
b.add(6) 
# b.add(7) 
# b.add(8) 
# b.add(9) 
# b.add(10) 
# b.add(11) 
print(b) #prints 6 only once as sets are collection of non repetative elements

 
#shows total number of items(lenght of set)
# print(len(b))

#removal of an item 
# b.remove(5)
# print(b)

# b.add([8,7,6]) # cant add a list in sets as they are unhashable 
# b.add((10,11,12)) # can add a tupple tho
# print(b)

# b.add({1:2}) # dictionary is not hashable i.e. you can change both dict & lists 

#b.pop removes a random item from set
# print(b.pop()) 


# b.union 
b.union({8,11}) 
print(b)
# b.intersection({2,3,4})
# # b.clear returns empty set 
# b.clear()
# print(b)