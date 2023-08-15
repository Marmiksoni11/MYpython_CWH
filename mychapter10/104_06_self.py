'''self is a parameter that passes automatically after calling an object(harry) 
 in other words harry = self''' 


# class employee:
#     company = "Google"
#     def getSalary(self):
#         print("Salary is 100k")

# harry = employee()

# #below lines are the same
# employee.getSalary(harry)
# harry.getSalary()



''' self = marmik , harry 
based upon which one is called/passed'''

class Employee:
    company = "google"
    def getSalary(self):
        print(f"{self.name}'s Salary in {self.company} is {self.salary}")
    

harry = Employee()
marmik = Employee()
harry.name = "Harry"
marmik.name = "marmik" 
harry.salary = 100000
marmik.salary = 100000
harry.getSalary()
marmik.getSalary()

Employee.company = "youtube"
marmik.salary = 150000
marmik.getSalary()






