#harrys way
# num = int(input("Enter your number: "))
# prime = True
# for i in range (2,num):
#     if(num%i==0):
#         prime = False
#         break
# if prime:
#     print("prime")
# else:
#     print("not prime")




#below is correct program 
# where it says 2 is prime and 1 is not a prime number.
num = int(input("Enter the NUM you want: "))

if num<2 and num!=1:
    print(num)
    print("NOT PRIME")

elif num==1:
    print(num)
    print("1 is a CO-PRIME NUMBER.")

elif num==2 :
        print(num)
        print("PRIME")
    
else:
    for i in range(2,num):
        if num%i==0:
            print(num)
            print("NOT PRIME")
            break
        
    else:
      print(num)
      print("PRIME") 