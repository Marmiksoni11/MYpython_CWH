class Employee:
    company = "google"
    

    #init only prints empl...created, bcoz conditions passed are true
    #as the arguments("harry,100,youtube") are passed in harry = Employee("")
    # but to print the details we have to pass another func and then print 
    def __init__(self, name ,salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created")

    def getDetails(self):
        print(f"the name of employee is {self.name}")
        print(f"the salary of employee is {self.salary}")
        print(f"the subunit of employee is {self.subunit}")

harry = Employee("harry", 100 , "Youtube")
harry.getDetails()# 2nd func that prints details 



