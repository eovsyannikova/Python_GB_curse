# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке
# Используется файл task2.txt
import os

path = (os.path.join(os.path.abspath(os.getcwd()), "task2.txt"))
line_count = 0
word_sum = 0
try:
    with open(path, "r", encoding="cp1251") as file:
        print('Файл открыт в режиме чтения')
        for line in file:
            line_count += 1
            word_count = 0
            for word in line.split():
                word_count += 1
                word_sum += 1
            # Выводим количество слов в конкретной строке
            print(f"{line_count}-я строка, в ней {word_count} слов(а)")
        # Выводим количество строк и слов во всем файле
        print("Всего {} строк, и {} слов ".format(line_count, word_sum))
except IOError:
    print("Произошла ошибка чтения файла!")


