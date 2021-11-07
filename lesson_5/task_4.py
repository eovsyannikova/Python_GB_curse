# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
# Файл с исходным содержимым task4_1.txt

import os


path_in = (os.path.join(os.path.abspath(os.getcwd()), "task4_1.txt"))
path_out = (os.path.join(os.path.abspath(os.getcwd()), "task4_2.txt"))

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
out_dict = {}

try:
    with open(path_in, "r") as file_in:
        print('Файл открыт в режиме чтения')
        # Читаем файл построчно
        for line in file_in.readlines():
            # Формируем словарь
            (key, value) = line.split(' — ')
            key_out = rus_dict[key]
            out_dict[key_out] = value
        print('Данные преобразованы')
    with open(path_out, "w", encoding='cp1251') as file_out:
        for key, value in out_dict.items():
            file_out.write('{} — {}'.format(key, value))
        print('Новый файл записан')
except IOError:
    print("Произошла ошибка чтения файла!")
