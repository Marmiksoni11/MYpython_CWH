
# pr 02 check if they have atleast 35 in each subject or total of 40% overall avg

hindi = int(input("Enter your Hindi Marks: "))
maths = int(input("Enter your Maths Marks: "))
english = int(input("Enter your English Marks: "))

if(hindi<34 or maths<34 or english<34):
    print("failed due to less than 33% in one of the subjects")
elif(((hindi+maths+english)/3)<40):
    print("failed due to less than 40% in total of all subjects")
else : 
    print("CONGRATULATIONS! You have Passed.") 