list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_ss = [z for z in list if list.count(z) < 2]
print(list_ss)