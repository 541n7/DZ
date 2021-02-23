seasons = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dic = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input('Номер месяца - '))
if month == 12 or month == 1 or month == 2:
    print(seasons[0])
    print(seasons_dic.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])
    print(seasons_dic.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])
    print(seasons_dic.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons[3])
    print(seasons_dic.get(4))
else:
    print('Такого месяца нету')