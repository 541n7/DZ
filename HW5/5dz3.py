with open('test3.txt', 'r') as file:
    sal = []
    po = []
    file = file.read().split('\n')
    for z in file:
        z = z.split()
        if int(z[1]) < 20000:
           po.append(z[0])
        sal.append(z[1])
print(f'Оклад меньше 20.000 {po}, \nСредний оклад {sum(map(int, sal)) / len(sal)}')