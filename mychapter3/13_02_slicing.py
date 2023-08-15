#CONCATENATION

a = "hello"
b = " marmik"
c = a+b #CONCATENATING TWO STRINGS
print(c)

#INDEXING
#starts from 0 from left side

d = "hello"
print(d[0])#prints h by 0 index, likewise, ello by 1 2 3 4 indices
print(d[1])
print(d[2])
print(d[3])
print(d[4])

#what if ?
print (d[:4])# --> this count blank as 0, same as (a[0:4])prints hell
print (d[0:])# ---> same as (a[0:6]), prints full word
e = "hello"
print (e[0],e[1],e[2]) #prints horizontally with spaces


#SLICING

f = "marmik"
print(f[0:4])#---> this includes 0 and exludes 4, so it prints, 0123
print (f[1:5])

# NEGATIVE INDEXING
#starts with -1 from right side 

g = "marmik soni"# space is also counted
print (g[-5:-1])#--> this is same as indexing, includes first exludes last i.e. 
#from space to n, .son

# also can be written like this
h = "sonimarmik"
i = h[0:6]
print(i)

#SKIPPING

j = "mycodeisgood"
print(j[0::1])# --> counts first character then skips none
print(j[0::2])# --> counts first character then skips 1
print(j[0::3])# --> counts first character then skips 2

