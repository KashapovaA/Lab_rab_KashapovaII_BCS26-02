print('Введите массив из 10 целых чисел')
n = input().split()
if not len(n) == 10:
    print('ошибка: нужно ввести 10 элементов')
else:
    lst = [i for i in n]
    for i in lst:
        if not i.isdigit():
            print('ошибка: нужно ввести числа')
        else:
            mlst = max(lst)
            mensh = []
            bolsh = 0
            for i in lst:
                if i < mlst:
                    mensh.append(i)
    print('Количество элементов меньших максимального элемента:', len(mensh))
    print('Количество элементов меньших максимального элемента:', bolsh)