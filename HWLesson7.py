# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# используйте split()
# Пример:
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# some_str = input('Введите строку => ')
# some_list = some_str.split(' ')
# list_vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# # print(some_list)
# some_set = set()
# for el in some_list:
#     count = 0
#     for item in el:
#         if item in list_vowel:
#             count += 1
#     some_set.add(count)
# if len(some_set) > 1: print('Пам парам')
# else: print('Парам пам-пам')

# Решение преподавателя
# def count_of_vowel(word):
#     vowel_set = {'а', 'о', 'е', 'у', 'э', 'ю', 'и', 'я', 'ё', 'ы'}
#     count = 0
#     for letter in word:
#         if letter in vowel_set:
#             count += 1
#     return count

# some_poem = input().split()
# for ind in range(len(some_poem) - 1):
#     if count_of_vowel(some_poem[ind]) != count_of_vowel(some_poem[ind + 1]):
#         print('Пам парам')
#         break
# else:
#     print('Парам пам-пам')

# Задача 36.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# import random

# some_list = [random.randint(1, 10) for _ in range(11)]
# print("Дан список =>", some_list)
# print("Количество различных элементов в списке равно", len(set(some_list)))