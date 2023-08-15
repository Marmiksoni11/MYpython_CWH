#convert marks to grades
# 90-100 = EX
# 80-90 = A
# 70-80 = B
# 60-70 = C
# 50-60 = D
# <50 = F


#myway
marks = int(input("Enter your marks: "))
if (marks>=90 and marks<=100):
    print("EX")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
else:
    print("F")


#harrys way
marks = int(input("Enter your marks: "))
if  marks>=90 :
    grade = "EX"
elif marks>=80 :
    grade = "A"
elif marks>=70 :
    grade = "B"
elif marks>=60 :
    grade = "C"
elif marks>=50 :
    grade = "D"
else:
    grade = "F"

print("your grade is " + grade)
