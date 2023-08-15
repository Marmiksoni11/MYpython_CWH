#range function : generates a sequence of numbers

for i in range(1,10):#includes 1(start) and excludes 10(stop)
    print(i)

for j in range(11):#starts from 0 by default 
    print(j)#prints 0 to 10 

for k in range(-11,11,2):# start(-11), stop(11), skip 1(as it is 2 at skip size)
    print(k)