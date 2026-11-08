n = input('Введите строку \n')
n2 = n.replace('a', '')
c = len(n) - len(n2)
print("Количество удаленных символов:", c)