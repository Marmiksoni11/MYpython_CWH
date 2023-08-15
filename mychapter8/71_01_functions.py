#functions


# a = [40,40,40,50]
# perc1 = (sum(a)/400)*100
# print(perc1)


 
# b = [45,50,40,50]
# perc2 = (sum(b)/400)*100
# print(perc2)
 


#in above program we need to repeat everytime to do this code
#so we use functions to make one code reusable over and over


# def percentage(marks):
#     return (sum(marks)/400)*100

# marks1 = [40,40,40,50]
# perc1 = percentage(marks1)

# marks2 = [45,50,40,50]
# perc2 = percentage(marks2)
# print(perc1,perc2)
 











def percentage(marks):
    return (sum(marks)/400)*100

marmikmarks = [40,50,60,90]
marmikperc = percentage(marmikmarks)

krishmarks = [90,80,70,85]
krishperc = percentage(krishmarks)

print(f"{marmikmarks} = {marmikperc}")
print(f"{krishmarks} = {krishperc}")