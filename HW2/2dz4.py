string = input('Введите предложение - ')
words = []
for z in range(string.count(' ') + 1):
    words = string.split()
    if len(str(words)) <= 10:
        print(words [z])
    else:
        print(words [z] [0:10])