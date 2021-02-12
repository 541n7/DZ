# а) итератор, генерирующий целые числа, начиная с указанного,
from itertools import count
zxc = int(input('Установите ограничение - '))
for z in count(int(input('Введите стартовое число - '))):
    print(z)
    if z > zxc or z == zxc:
        break

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import cycle
cc = 0
list = [True, 'ABC', 123, None]
for x in cycle(list):
    print(x)
    cc += 1
    if cc == 12:
        break