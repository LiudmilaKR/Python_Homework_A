# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input('Введите первый элемент a1 => '))
# d = int(input('Введитe разность d => '))
# n = int(input('Введиет количество элементов n => '))

# some_list = [a1 + (i - 1) * d for i in range(1, n)]
# print(some_list)
# Вариант преподавателя
# some_list = [i for i in range(a1, a1 + (n -1) * d + 1, d)]

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# n = int(input('Введите количество элементов массива n => '))
# minn = int(input('Введите число-минимум => '))
# maxx = int(input('Введите число-максимум => '))

# some_list = [random.randint(1, 100) for _ in range(n)]
# print('Массив чисел =>', some_list)

# res_list = list()
# for i in range(len(some_list)):
#     if minn < some_list[i] < maxx:
#         res_list.append(i)

# print(res_list)
# Вариант преподавателя
some_list = [int(input('Введите элемент списка: ')) for _ in range(int(input('Введите количество элементов: ')))]
a = int(input())
b = int(input())
for ind in range(len(some_list)):
    if a <= some_list[ind] <= b:
        print(ind)