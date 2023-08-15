num = int(input("Enter your number: "))
class Calculator:
    def __init__(self,num):
        self.num = num
       
    def square(self):
      print(f"The square of {self.num} is {self.num**2}") 
   
    def cube(self):
      print(f"The cube of {self.num} is {self.num**3}") 
       
    def squareRoot(self):
      print(f"The Square Root of {self.num} is {self.num**0.5}") 

a = Calculator(num)
a.square()
a.cube()
a.squareRoot()
