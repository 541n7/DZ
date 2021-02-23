name = input('Имя - ')
surname = input('Фамилия - ')
year = (input('Год рождения - '))
city = input('Город - ')
email = input('Email - ')
telephone = input('Номер телефона - ')
def my_func(name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname, name, year, city, email, telephone))