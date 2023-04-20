# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def task_18():
    n = int(input('Введите число N: '))
    a = []
    while len(a) < n:
        a += [int(i) for i in input().split()]
    x = int(input('Введите число X: '))
    min_diff = abs(a[0] - x)
    min_diff_index = 0
    for i in range(1, len(a)):
        diff = abs(a[i] - x)
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i
    print(a[min_diff_index])

task_18()