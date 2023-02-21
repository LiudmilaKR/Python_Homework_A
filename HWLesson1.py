# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input('Введите трехзначное число => '))
# if (99 < n < 1000):
#     print(f'Сумма числа {n} = {n // 100 + (n // 10) % 10 + n % 10}')
# else:
#     print('Вы ввели некорректное число!')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# Пояснение к решению:
# x + 2y = S, x = 4y => y = s/6, x = 2S/3

# s = int(input('Введите общее количество журавликов => '))
# print(f'{s} => {int(s / 6)}   {int(2 * s / 3)}   {int(s / 6)}')

# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# n = str(input('Введите номер билета => '))
# if (len(n) == 6):
#     if ((int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5]))): print('Билет счастливый!')
#     else: print('Билет не счастливый...')
# else:
#     print('Вы ввели некорректное число!')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
# n = int(input('Введите n => '))
# m = int(input('Введите m => '))
# k = int(input('Введите k => '))
# for i in range(1, n):
#     if (k == i * m):
#         print('yes')
#         break
#     else: continue
# else:
#     for j in range(1, m):
#         if (k == j * n):
#             print('yes')
#             break
#         else: continue
#     else: print('no')