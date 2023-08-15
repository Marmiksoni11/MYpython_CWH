#censor donke

'''with open('sample.txt','r') as f :
    t  = f.read()
    t =  t.replace("donkey","#$@#")
with open('sample.txt','w') as f:
    f.write(t)'''

#censor words from the list
s = ["donkey","bozo","gadha","kutta","kamina"]
with open('censor2.txt','r') as f :
    t  = f.read()
    for word in s:
     t =  t.replace(str(word),"#$@#")#checks each word
with open('censor2.txt','w') as f:
    f.write(t)

