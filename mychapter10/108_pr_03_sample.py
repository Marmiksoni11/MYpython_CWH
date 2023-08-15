from random import sample


class Sample:
    a = 5
   
obj = Sample()
obj.a  = 0 
print(Sample.a) #answer : it wont change as the obj i.e. instance attribute a
#  in obj.a is 0 , but  
# class attribute a in Sample.a is not 0 specified  


'''to change it do the below'''
Sample.a  = 0
print(Sample.a)

