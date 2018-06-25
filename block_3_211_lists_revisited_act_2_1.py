a_list = [2, 5, 1]
length = len(a_list)
print ('This list has length', length)
for value in a_list:
    if value ==5:
        print ('This list contains the number 5')
last = a_list[length -1]
if last == 1:
    print ('The last value in the list is 1')
a_list = a_list + [0]
length = len(a_list)
last = a_list[length -1]

assert last == 0



