a = {
    "marmik" : "is my name",
    1 : 2,
    "fast" : "nah slow"
}
a["fast"] = ["0,1,2,3,3,4"]
print(type(a))

updatedict = {
    "soni": "is mah surname",
    "123" : "is 456",
    3 : 4,
    "fast" : "yeh slow"
}
#methods
a.update(updatedict)
print(a)

print (a.keys())
print(a.get("soni2"))
print(a.values())
print(a.items())