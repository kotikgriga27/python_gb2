# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            indexes.append(i)
    return indexes

n = int(input("Введите количество элементов списка: "))

# Сгенерировать список из 10 случайных целых чисел от 1 до 100
lst = [random.randint(1, 100) for _ in range(n)]
print("Список: ", lst)

min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

indexes = find_indexes(lst, min_val, max_val)
print("Индексы элементов списка, значение которых находится в диапазоне от", min_val, "до", max_val, ":", indexes)


