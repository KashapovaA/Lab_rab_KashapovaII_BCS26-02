print("Введите целое число:")
n = input()
if not n.isdigit():
    print('ошибка')
else:
    n = int(n)
    if n <= 1:
        print('ошибка')
    else:
        k = 1
        while 5**k <= n:
            k += 1
        print("наименьшее целое число k, при котором выполняется неравенство 5**k > n:", k)