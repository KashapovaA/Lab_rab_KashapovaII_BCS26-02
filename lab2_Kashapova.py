a = False
while not a:
    m1 = input()
    if m1.isdigit():
        m = int(m1)
        a = True
    else:
        print('Это не число, введите значение массы')

if m < 1 or m > 10000:
    print('это значение массы недопустимо')
else:
    print('Выберите тип смеси (1 - бетон, 2 - керамика, 3 - сплав):')
    c = int(input())
match c:
    case 1:
        smes = 'бетон'
        cement = 0.15
        pesok = 0.35
        csheben = 0.5
        t = cement + pesok + csheben
        h = 1
    case 2: 
        smes = 'керамика'
        glina = 0.6
        pesok = 0.25
        dob = 0.15
        t = glina + pesok + dob
        h = 1
    case 3: 
        smes = 'сплав'
        Cu = 0.7
        Zn = 0.25
        Pb = 0.05
        t = Cu + Zn + Pb
        h = 0

    case 0:
        print('неверный номер типа смеси')
if h == 1:
    if not (t - 1.0) < 0.0001:
        print('сумма долей для смеси не равна 1')
    else:
        if m < 100:
            clas = 'малая партия'
        elif 100 <= m <= 1000:
            clas = 'средняя партия'
        else:
            clas = 'крупная партия'
        print('тип смеси:', smes)
        print('класс партии:', clas)
        print('массы компонентов:')

        match c:
            case 1:
                print('цемент:', m * cement, 'кг')
                print('песок:', m * pesok, 'кг')
                print('щебень:', m * csheben, 'кг')
            case 2:
                print('глина:', m * glina, 'кг')
                print('песок:', m * pesok, 'кг')
                print('добавка:', m * dob, 'кг')
            case 3:
                print('медь:', m * Cu, 'кг')
                print('цинк:', m * Zn, 'кг')
                print('свинец:', m * Pb, 'кг')
                
