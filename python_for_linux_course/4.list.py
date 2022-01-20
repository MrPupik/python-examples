[1, 2, 3, 4, 5, 6]
lst = ['sldgf', 6545, False]

for something in lst:
    print(something)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10000]
print('first ' + str(lst[0]) + '. and last: '+str(lst[-1]))
print('and the fifth !: ' + str(lst[4]))
print('only even indexes: ' + str(lst[1::2]))
print('second to forth: '+str(lst[1:4]))
lst[1:3] = [0, 0]
print('changed list: ', lst)


# more on lists

# easy way to copy list/string

# copy a slice
lst2 = lst[2:6]

# copy full
lst2 = lst[:]

# change a part
lst2[1:3] = [-1, -1]

# change + shorten !
lst2[1:3] = [-1]

# delete one
lst2[5] = []


# a lot can be done with function !!!
# add to the end:
lst.append(5)
# pop 
lst.pop()
