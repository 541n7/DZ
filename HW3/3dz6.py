def int_func(word):
    small = word[0]
    big = chr(ord(small) - ord('a') + ord('A'))
    return big + word[1:]
s = input('Введите слово - ').split()
res = []
for word in s:
    res.append(int_func(word))
print(' '.join(res))