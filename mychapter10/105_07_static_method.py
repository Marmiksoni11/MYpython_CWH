class Employee:
    company = "google"
    def getSalary(self, signature):
        print(f"{self.name}'s Salary in {self.company} is {self.salary}\n{signature}")
    #in above signature is an argument and the first argument in the function
    


    #how to call a function in a class without using self 
    '''@satic method is used to do that'''
    '''however it can be used only for NON-Fstrings'''
    @staticmethod #this is decorator 
    def greet():
        print("Good Morning, Sir!")

    @staticmethod  
    def time():
        print("the time is 9AM in morning.")

harry = Employee()
marmik = Employee()

harry.name = "Harry"
marmik.name = "marmik" 

harry.salary = 100000
marmik.salary = 100000

# below  signature = "Thanks!" in the function call
#no need to add self as it is automatically called
harry.getSalary("Thanks!") 
marmik.getSalary("Thanks!")

Employee.company = "youtube"

marmik.salary = 150000
marmik.getSalary("Thanks!")

harry.greet()
harry.time()