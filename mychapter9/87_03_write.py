f = open('another.txt', 'w')
f.write("please write in the file")#creates a new file and writes 
#if it does not exist
f.close()

f = open('another.txt', 'a')
f.write("i am appending")#appends the line the number of times u run it
#appended 5 times 
f.close()


f = open('another.txt', 'w')
f.write("please write in the file") 
f.write("please write in the file2") 
f.write("please write in the file3") #if we remove these lines
# the lines will be removed from the file too
f.write("please write in the file4") 
f.write("please write in the file5") 
f.close()
