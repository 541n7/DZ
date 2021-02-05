rating = [7, 5, 3, 3, 2]
print('Рейтинг - ', rating)
num = int(input('Введите число - '))
while num != 000:
    for z in range(len(rating)):
        if rating[z] == num:
            rating.insert(z + 1, num)
            break
        elif rating[0] < num:
            rating.insert(0, num)
        elif rating[-1] > num:
            rating.append(num)
        elif rating[z] > num and rating[z + 1] < num:
            rating.insert(z + 1, num)
    print('Рэйтинг - ', rating)
    num = int(input("Введите число - "))