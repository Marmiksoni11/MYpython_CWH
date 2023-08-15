#i made the files to with seires name this1,this2
#but the ques says i  have to copy the content from a pre-existing file called 'this.txt' 


# #my way, is not correct but isnt wrong either
# for i in range(1,3):
#     with open(f'this.text{i}','w') as f:
#         f.write(f"{i}")



#harrys way
with open('this.txt','r') as f:
         content = f.read()
with open('copy.txt','w') as g:
         g.write(content)