#use open function to read the content of a file!
# f = open("sample.txt","r")




f = open('sample.txt')#by default the mode is r 
#data = f.read()
data = f.read()#reads only first 5 chars
print(data)
f.close

# modes
# 'rb' - reads in Binary
# 'rt'/'r'- rt /r same meaning read in text mode
# 'w' - open for writing
# 'a' - open for appending
# '+' - open for updating(both read and write)

# a = open('sample.txt')
# data = a.read()
# print(data)
# a.close

