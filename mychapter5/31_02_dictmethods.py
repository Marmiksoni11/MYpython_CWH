#dictionary methods

mydict = {
    "marmik" : "what is your name, again?",
    "fast" : "damn, he is fast",
    "slow" : "he isnt that slow tho",
    "coder" : "marmik is a coder now",
    1 : 2
}
print(mydict["marmik"])
print(mydict.keys())#method1, prints all the keys in a list

print(type(mydict.keys())) # dict not a list so can be conv into a list,
print(list(mydict.keys()))
print(type(list(mydict.keys()))) # now a list

print(mydict.values()) #method2 prints values in keys

print(mydict.items())#method3 print every item(everything) in order with comas

 #method4 update a list,(adding key-value pairs) from updatedict
 #also values of existing keys can be updated(replaced) like in marmik
 # what is... replaced with soni 
updatedict = {
    "midoriya" : "izuku",
    "marmik" : "soni"
}
mydict.update(updatedict)
print(mydict)

#method5 imp, interview que, .get
#both .get and normal[] dict gives same output
# but if the key is not present in the dict then [] throws error
# but .get returns "None" due to error 
#so it saves from error showcase
'''like in this case output is same'''
print(mydict.get("marmik"))  
print(mydict["marmik"]) 

'''but here the difference is'''
print(mydict.get("marmik2"))  #returns none as marmik2 isnt present in the dict
print(mydict["marmik2"]) # thorws an error as marmik2 isnt present in the dict