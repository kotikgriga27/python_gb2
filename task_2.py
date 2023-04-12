# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = input('Введите трёхзначное число: ')
l = len(number)
number = int(number)

if l == 3:
    digit1 = number // 100
    digit2 = (number % 100) // 10
    digit3 = number % 10

    # Вычисление суммы цифр
    sum_of_digits = digit1 + digit2 + digit3
    print(sum_of_digits)
else:
    print('Введено не трёхзначное число!')