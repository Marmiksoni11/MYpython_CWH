'''  *
   * * *
 * * * * * '''

n = 3 #three rows
for i in range(3):
    print(" " * (n-i-1), end ="")#left spacing
    print("*" * (2*i+1), end ="")#middle stars
    print(" " * (n-i-1))#right spacing

#also ,end="" will help removing extra spaces in the loop