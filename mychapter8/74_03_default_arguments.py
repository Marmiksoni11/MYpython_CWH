#defualt arguments
#below 'name' is assigned with "stranger" as a default arg
#if someone dont specify the stringvalue in name i.e. greet()
# than name will count "stranger" as the default value

def greet(name="stranger"):
    print("hello!", name)
greet("marmik")
greet("krish")
greet() #prints defualt arg

