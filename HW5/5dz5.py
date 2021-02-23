def summ():
    try:
        with open('test5.txt', 'w+') as file:
            line = input('Введите числа через пробел - ')
            file.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка!! Введено не число')
summ()