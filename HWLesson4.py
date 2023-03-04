# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# import random

# n = int(input("Введите количество элементов первого набора => "))
# m = int(input("Введите количество элементов второго набора => "))

# def get_list(k: int) -> list:
#     some_list = []
#     for _ in range(k):
#         some_list.append(random.randint(1, 10))
#     return some_list

# list1 = get_list(n)
# list2 = get_list(m)
# print(f'Первый набор чисел из {n} элементов => {list1}')
# print(f'Второй набор чисел из {m} элементов => {list2}')
# set1 = set(list1)
# set2 = set(list2)
# set_rez = set1.union(set2)

# print('Числа из обоих наборов без повторений => ', set_rez)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# import random

# N = int(input("Введите количество кустов на грядке => "))

# some_list = []
# for i in range(N):
#     ai = random.randint(1, 100)
#     print(f'на {i + 1}-м кусте выросло {ai} ягод')
#     some_list.append(ai)

# maxx = some_list[0] + some_list[N - 1] + some_list[N - 2]
# for i in range(1, N - 2):
#     temp = some_list[i] + some_list[i + 1] + some_list[i + 2]
#     if temp > maxx:
#         maxx = temp
# print(maxx, 'ягод может собрать за один заход собирающий модуль')