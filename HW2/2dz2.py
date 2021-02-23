elements = int(input('Количество элементов - '))
spisok = []
z = 0
x = 0
while z < elements:
    spisok.append(input('Значение елемента = '))
    z += 1
for c in range(int(len(spisok)/2)):
    spisok[x], spisok[x + 1] = spisok[x + 1], spisok[x]
    x += 2
print(spisok)