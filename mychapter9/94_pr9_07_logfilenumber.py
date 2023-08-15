#continue from pr6,
#check the line number in python


content = True
i = 1 #starting the while loop from 1, and shows the number of lines at the end of loop
with open('IBMlogfile.txt') as f :
    while content : #using the while loop for looping readline method,
        #while keeps executing until the loop is turns false(i.e. after reading all lines)
       content = f.readline()
       if  "python" in content.lower():#checking if "python" is there
         print(f"Mining successful: The word 'python' is PRESENT in the line {i}")
         print(content)
       i += 1 #reads the next line