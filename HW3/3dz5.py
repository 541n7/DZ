def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число(-а) (q для выхода) - ').split()
        res = 0
        for z in range(len(number)):
            if number[z] == 'q' or number[z] == 'Q':
                ex = True
                break
            else:
                res += int(number[z])
        sum_res += res
        print('Сумма -', sum_res)
    print('Конечная сумма - ', sum_res)
sum()