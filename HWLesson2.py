# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# import random
# n = int(input('Введите число монеток => '))
# orel = random.randint(1, n)
# reshka = n - orel

# print(f'У нас {n} монет, из которых {orel} орлов и {reshka} решек.')
# if (orel > reshka): print (f'Минимальное количество монет, которые необходимо перевернуть {reshka}')
# else: print (f'Минимальное количество монет, который необходимо перевернуть {orel}')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# x+y=s, xy=p => необходимо решить квадратное уравнение y**2-sy+p = 0, и потом x=s-y

# import math
# s = int(input('Введите сумму чисел X и Y => '))
# p = int(input('Введите произведение чисел X и Y => '))

# d = math.sqrt(s * s - 4 * p)
# if (d % 1 == 0):
#     y = (s + d) / 2
#     x = s - y
#     print(f'Одно натуральное число {int(x)} другое {int(y)}')
# else: print('Числа не натуральные!')

# Эталонное решение (я, похоже, сильно усложнила... :)
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
        # # print('i=', i, '   j=', j)
#         if x == i + j and y == i * j:
#             print(i, j)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# N = int(input('Введите число N => '))
# degree = 1
# i = 1
# flag = True
# while flag:
#     if degree < N:
#         print(degree, end=' ')
#         degree = 2 ** i
#         i += 1
#     else: flag = False

# Эталонное решение
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i, end=' ')
#     i += 1

