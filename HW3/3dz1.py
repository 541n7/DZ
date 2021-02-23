def division(*args):
    try:
        num1 = int(input("Введите делимое - "))
        num2 = int(input("Введите делитель - "))
        res = num1 / num2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Делить на 0 нельзя"
    return res
print(division())