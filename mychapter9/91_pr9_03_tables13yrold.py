
#my try

# n = 2
# for i in range(1,11):
#     table = i*n
#     h = (f"{n} X {i} = {table}")
#     # print(h)
# # n = n + 1    
# # if n == 2:
# with open('tableof2.txt', 'w') as t:
#     f = t.write(str(h))
# if n == 3:
#     with open('tableof3.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 4:
#     with open('tableof4.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 5:
#     with open('tableof5.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 6:
#     with open('tableof6.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 7:
#     with open('tableof7.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 8:
#     with open('tableof8.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 9:
#     with open('tableof9.txt', 'w') as t:
#         f = t.write(str(h))
# if n == 10:
#     with open('tableof10.txt', 'w') as t:
#         f = t.write(str(h))



# harrys way
for i in range(2,21):
    with open (f'tables/table of {i}', 'w') as f:
         for j in range(1,11):
           f.write(f"{i} X {j} = {i*j}")
           if j !=10:
            f.write("\n")
    
