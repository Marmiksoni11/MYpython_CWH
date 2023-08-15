#remove and strip

def rem_and_strip(string, word): #funtion usage pattern string followed by a word
    newstr = string.replace(word,"")
    return newstr.strip() #strips 'string' as it is inside newstr
this = "    marmik is good     " 
n = rem_and_strip(this, "marmik") # rem_and_strip(string,word) and word will
#be replaced by ""/blank
print(n)



#my practice
def rem_str(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()
well = "    oh my god      "
n = rem_str(well, "oh")
print(n)
