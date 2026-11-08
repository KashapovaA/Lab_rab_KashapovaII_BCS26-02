print("Введите целое число, меньшее 51:")
a = input()
if not a.isdigit():
    print('ошибка')
if not 0<= int(a) <= 50:
    print('ошибка')
else:
    su = 0
    for i in range(int(a), 51):
        su += i**2
    print("сумма квадратов всех целых чисел от а до 50:", su)