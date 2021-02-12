from itertools import count
from math import factorial

def zxc():
    for z in count(1):
        yield factorial(z)

qwe = zxc()
x = 0
for i in qwe:
    if x < 15:
        print(i)
        x += 1
    else:
        break