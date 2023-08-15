class employee : 
    company = "Google"
    salary = 100

harry = employee()
rajni = employee()

print(harry.company)

harry.company = "youtube"

print(harry.company)

#salary before from salary attribute in class employee 
print(harry.salary)
print(rajni.salary)

#now lets change the salaries for both employees by creating instance attributes
#for both objects
harry.salary = 200
rajni.salary = 300

print(harry.salary)
print(rajni.salary)


#below line throws an error as address is not present in instance/class
  