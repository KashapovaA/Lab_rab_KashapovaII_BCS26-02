print('Введите массив из 10 целых чисел')
n = input()
lst = [x for x in n.split()]
if not len(lst) == 10:
    print('ошибка: нужно ввести 10 элементов')
else:
    for i in lst:
        if not i.isdigit():
            print('ошибка: нужно ввести числа')
        else:
            su = 0
            for i in lst:
                if int(i) > 5:
                    su += int(i)
    print('Сумма чисел, которые > 5:', su)