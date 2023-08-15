# check if python is there in the log file?

with open('IBMlogfile.txt','r')as f :
    t = f.read()
    if "python" in t.lower():#lower bcos it is case sensitive
        print("Mining successful: The word 'python' is PRESENT in the LOG file")
    else:
        print("Mining successful: The word 'python' is NOT PRESENT in the LOG file")






# # do the above for the given list
# words = ["python","marmik","damn"]
# with open('IBMlogfile.txt','r')as f :
#     word = f.read()
    # for word in words:
    #    if "python" in word:
    #      print(f"Mining successful: The word 'python' is present in the LOG file")
    #    elif "marmik" in word:
    #      print(f"Mining successful: The word 'marmik' is present in the LOG file")
    #    elif "damn" in word:
    #      print(f"Mining successful: The word 'damn' is present in the LOG file")
