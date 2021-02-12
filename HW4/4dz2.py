list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_ss = [z for num, z in enumerate(list) if list[num - 1] < list[num]]
print('Исходный список', list)
print('Результат', list_ss)