#how to input a list
list = []

n = int(input("Enter number of elements: "))#number of elements

for i in range(0,n):
    elements = int(input("Enter marks of four subjects out of 100: "))#input elements
    list.append(elements)#adds elements
    print(list)   



#percent calculator using def function

def percentage(list):
    return (sum(list)/400)*100
perc = percentage(list)
print(perc)


