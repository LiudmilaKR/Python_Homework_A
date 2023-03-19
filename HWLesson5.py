# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -.
# Вычислите результат.
# Пример
# Ввод
# 8-5+2-1
# Вывод
# 4
# some_str = '-8-5 +2-1'
# some_str = some_str.strip().replace(' ', '')

# sum = 0
# if some_str[0] == '-':
#     if some_str[2] == '+': sum = (-1) * int(some_str[1]) + int(some_str[3])
#     elif some_str[2] == '-': sum = (-1) * int(some_str[1]) - int(some_str[3])
#     for i in range(4, len(some_str) - 1):
#         if some_str[i] == '+':
#             sum += int(some_str[i + 1])
#         elif some_str[i] == '-':
#             sum += (-1) * int(some_str[i + 1])
# else:
#     sum = int(some_str[0])
#     for i in range(1, len(some_str) - 1):
#         if some_str[i] == '+':
#             sum += int(some_str[i + 1])
#         elif some_str[i] == '-':
#             sum += (-1) * int(some_str[i + 1])

# print(f'Результат выражения ({some_str}) равен {sum}')
# Решение преподавателя
# some_str = input('Введите пример ')
# res = 0
# znak = ''
# for el in some_str:
#     if el.isdigit():
#         if znak =='-':
#             res -= int(el)
#         else:
#             res += int(el)
#     else:
#         znak = el
# print(res)

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите слова из строки по одному.

# Пример 1
# Ввод
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод

# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

# sstr = 'Здравствуйте! Я - Ваша тётя!'
# i = 0
# temp = 0
# while i < len(sstr):
#     if sstr[i] == ' ':
#         print(sstr[temp : i])
#         temp = i + 1
#         i += 1
#     else: i += 1
# print(sstr[temp : len(sstr)])

# Решение преподавателя
# some_str = 'Здравствуйте! Я - Ваша тётя!'
# some_str = some_str + ' '
# word = ''
# for letter in some_str:
#     if letter != ' ':
#         word += letter
#     else:
#         print(word)
#         word = ''

# # Решение через split
# print(*some_str.split(), sep='\n')

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# A, B = input('Введите числа A и B через пробел: ').split()
# A, B = int(A), int(B)

# def rate(a: int, b: int) -> int:
#     # r = 1
#     if b == 0:
#         return 1
#     else:
#         return rate(a, b - 1) * a
    
# print(f'Число {A} в степени {B} равно {rate(A, B)}')