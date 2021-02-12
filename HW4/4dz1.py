def profit():
    try:
        hours = float(input('Вырбаботка в часах - '))
        salary = int(input('Ставка в час - '))
        bonus = int(input('Премия - '))
        res = hours * salary + bonus
        print('Зарплата сотрудника - ',  res)
    except ValueError:
        return print('Ошибка!!!')
profit()