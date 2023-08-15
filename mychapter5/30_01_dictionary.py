
#DICTIONARY 

mydict = {
    "fast" : "in a quick manner",
    "marmik" : "a new python coder ", #keep dictionary is lowercase first
    #letter for ease of access
    "marks" : [22,22,12,12,12],
    "float" : 12.2,
    "bool" : True,
    "int"  : 1122,
    "anotherdict" : {"soni" : "marmik"} #dict in dict /Nested dictionaries 
}
print(mydict["fast"])
print(mydict["marmik"])
print(mydict["marks"])
print(mydict["float"])
print(mydict["bool"])
print(mydict["int"])
print(mydict["anotherdict"])# prints its value as a whole
print (mydict["anotherdict"]["soni"])#likewise print value inside the dict too
  

# print(type(mydict["float"]))
# print(type(mydict["marmik"]))
# print(type(mydict["bool"]))
# print(type(mydict["fast"]))
# print(type(mydict["marks"]))
# print(type(mydict["int"]))
print(type(mydict["anotherdict"])) #this shows <class 'dict'>

#PROPERTIES
'''1. it is unordered '''
'''2. it is mutable'''
'''3. it is indexed'''
'''4. cannot contain duplicate keys'''

# ex for '''2.'''

mydict["marks"] = [12,22,33,44,55] #mutable 
print(mydict["marks"]) 

