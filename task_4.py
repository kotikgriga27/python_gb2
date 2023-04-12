s = int(input('Введите количество журавликов: '))

if s % 6 == 0:
    a = (s // 3) // 2
    b = s - s // 3
    print("{} {} {}".format(a, b, a))
else:
    print('Error!')