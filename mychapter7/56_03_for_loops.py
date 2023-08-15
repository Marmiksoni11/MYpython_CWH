#for loops are used to iterarte thru a sequence like list,tuple or string


#does the same work like previous while loop
#but in a more convinient manner(easily)
l = [12,33,44,55,12,90,00]
for item in l:
    print(item)
    print(type(item))

i = ("marmik","krish","kavya","mahi")
for item in i:
    print(item)
    print(type(item))
    
j = "lala","kaka","shsha","topa"
for item in j:
    print(item)
    print(type(item))

# when a strings are stored in tuple , and then moved to 'item'
# then they become strings not tuple  
i = ("marmik","krish","kavya","mahi")
for item in i:
    print(type(i))
    print(item)
    print(type(item))