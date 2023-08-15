#pr 02 celcius to farenheit


#my way 
# def far(cel):
#     return (cel * (9/5))+32
# cel=100
# temp = far(cel)
# print(temp)



# #harrys way
# def far(cel):
#     return (cel * (9/5))+32
# c = 0 #alter the value accordingly
# f = far(c)
# print(f)


#taking input from user my way
cel = int(input("Enter the celsius temp: "))
def far(cel):
    return (cel * (9/5))+32
temp = far(cel)

print(str(cel) + " degrees celsius is " + str(temp)+" degrees farenheit")
