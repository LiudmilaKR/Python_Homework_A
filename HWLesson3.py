# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random

# N = int(input("Введите натуральное число N => "))
# x = int(input("Введите число x => "))

# def createArr(n: int, a: int) -> list:
#     some_array = []
#     for _ in range(n):
#         some_array.append(random.randint(1, a))
#     return some_array

# array = createArr(N, x)
# print(array)

# # вариант 1
# # count = 0
# # for el in array:
# #     if el == x: count +=1 

# # вариант 2
# count = array.count(x)
# print(f'Число {x} встречается {count} раз в массиве')


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
# import random
# N = int(input("Введите натуральное число N => "))

# def createArr(n: int) -> list:
#     some_array = []
#     for _ in range(n):
#         some_array.append(random.randint(1, n))
#     return some_array


# array = createArr(N)
# print(array)
# x = int(input("Введите число x => "))

# if x in array: print(f'{x} самый близкий по величине элемент к x = {x}')
# else:
#     flag = True
#     temp = 1
#     while True:
#         a = x + temp
#         b = x - temp
#         if a in array:
#             print(f'{a} самый близкий по величине элемент к {x}')
#             flag = False
#             break
#         elif b in array:
#             print(f'{b} самый близкий по величине элемент к {x}')
#             flag = False
#             break
#         else:
#             temp += 1

# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# some_dict = {1: ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'), \
#              2: ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'), 3: ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'), \
#              4: ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'), 5: ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч'), \
#                 8: ('J', 'X', 'Ш', 'Э', 'Ю'), 10: ('Q', 'Z', 'Ф', 'Щ', 'Ъ')}
# some_string = input('Введите слово => ')
# sum = 0
# some_string1 = some_string.upper()
# for item in some_string1:
#     for k, v in some_dict.items():
#         if item in v:
#             sum = sum + k
# print(f'Слово <{some_string}> весит {sum} очков')
