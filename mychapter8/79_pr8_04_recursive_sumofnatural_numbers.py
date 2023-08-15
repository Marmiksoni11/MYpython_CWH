# n= 5
# 1+2+3+4+5



#n! = (n-1)*n
#sum(n)= sum(n-1)+n


n = int(input("Enter the value of n: "))
def natural(n):
    if n==0:
      return 0
    return natural(n-1) + n
    
s = natural(n)
print(s)






