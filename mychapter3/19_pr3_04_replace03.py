b = "my name is  marmik."
doubleSpaces = b.find("  ")
print(doubleSpaces)
print(b.replace("  "," "))

#or HARRYS WAY , only use replace function

b = "my name is     marmik."
b = b.replace("     "," ")
print(b)