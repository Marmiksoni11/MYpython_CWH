class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,post):
        self.name = name
        self.salary = salary
        self.post = post
        print("Programmer added Successfully!")
    
    def getDetails(self):
        print(f"\nThe name of {self.company} Programmer is {self.name}.")
        print(f"The salary of Programmer is {self.salary}")
        print(f"The post of Programmer is {self.post}")

harry = Programmer("Harry",100000,"Manager")
Marmik = Programmer("Marmik",100000,"Senior")

harry.getDetails()

Marmik.getDetails()

