def my_func(n1 , n2, n3):
    if n1 >= n3 and n2 >= n3:
        return n1 + n2
    elif n1 > n2 and n1 < n3:
        return n1 + n3
    else:
        return n2 + n3
print('Сумма - ',(my_func(int(input("Первое число - ")), int(input("Второе число - ")), int(input("Третье число - ")))))