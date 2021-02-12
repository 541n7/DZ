from functools import reduce
def func(zz, z):
    return zz * z
print('Список четных значений', [z for z in range(99, 1001) if z % 2 == 0])
print('Результат произведения всех элементов списка', reduce(func, [z for z in range(99, 1001) if z % 2 == 0]))