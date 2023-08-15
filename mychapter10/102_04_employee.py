class employee:
    company = "Google"
    salary = 100

''' here company is a class attribute harry,marmik,krish are  instances
 in the class employee 
'''


harry = employee() 
marmik = employee()
krish = employee()

print(marmik.company)

employee.company = "Youtube" #for all employees

kavya = employee()
mahi = employee()

print(marmik.company) #changed attribute
print(mahi.company)

harry.company = "Samsung" #only changes company of harry

print(harry.company)
print(marmik.company)



harry.salary = 300 
marmik.salary = 400
krish.salary = 500
print(harry.salary)
print(marmik.salary)
print(krish.salary)
print(employee.company)


