
#my way
with open('this.txt','r')as f:
    content1 = f.read()

with open('copy.txt','r')as g:
    content2 = g.read()

if content1 == content2:
    print("they are identical")
else:
    print("they aren't identical")


#harrys way
file1 = 'this.txt'
file2 = 'copy.txt' 
with open(file1) as f:
    content1 = f.read()

with open(file2) as g:
    content2 = g.read()

if content1 == content2:
    print("they are identical")
else:
    print("they aren't identical")
