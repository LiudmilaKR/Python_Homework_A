# 1.Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние 
# строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines: int, file: str):
#     if lines > 0:
#         with open (file, 'r', encoding='utf-8') as data:
#             my_text = data.readlines()
#             for ind in range(len(my_text) - lines, len(my_text)):
#                 print(my_text[ind])
#     else: print('Количество строк введено некорректно')

# path_file = 'HomeworkA/article.txt'
# num = int(input('Введите количество строк => '))
# read_last(num, path_file)

# 2.Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, имеющее 
# максимальную длину (или список слов, если таковых несколько).

# def longest_words(file: str):
#     with open (file, 'r', encoding='utf-8') as data:
#         my_text = data.readlines()
#         max_len_elem = ''
#         for item in my_text:
#             if len(item) > len(max_len_elem):
#                 max_len_elem = item
#         # print(max_len_elem)
#     with open ('HomeworkA/result.txt', 'w', encoding='utf-8') as data1:
#         data1.write(max_len_elem)

# path_file = 'HomeworkA/article.txt'
# longest_words(path_file)