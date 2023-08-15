# #continue Statement

# #here the loop goes on till 4 and keeps printing i value
# # however when it comes to 5 it continues looping without printing, so it skips 5
# #prints from 0-4 and 6-9

# for i in range(10):
#     if i==5:
#      continue
#     print(i)



# l = [12,23,44,73,2]
# for item in l:
#     if item==l[3]:#skipped 73 at 3rd index
#         continue
#     print(item)


#program to print odd and even numbers

for i in range(10):
    if i % 2 == 0: #returns even values
      continue #skips even values
    print(i)

for i in range(10):
    if i % 2 != 0: #returns odd values 
         continue #skips odd values
    print(i)


# i % 2 == 0 means ,i = 2 divide by 2 gives remainder 0 print i
# likewise, i % 2 ==0 means ,i = 4 divide by 2 gives remainder 0 print i 

