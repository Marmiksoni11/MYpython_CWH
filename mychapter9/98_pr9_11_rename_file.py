#rename a file means
# make a new file with given name and with identical content
#delete the old file

import os #importing the os module

oldname = 'sample2.txt'
newname = 'renamed_by_python.txt'
#transfering the content
with open(oldname,'r') as f :
    content = f.read()
with open (newname,'w') as g:
     g.write(content)

os.remove(oldname)#os method that removes the file