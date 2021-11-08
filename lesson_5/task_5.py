# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import os

path = os.path.join(os.getcwd(), "task_5.txt")
print(path)
num_list = []
try:
    with open(path, "w", encoding='utf-8') as file_out:
        str_out = input('Введите числа через пробел: ')
        file_out.write(str_out)
    with open(path, "r", encoding='utf-8') as file_in:
        num_list = [float(word) for line in file_in.readlines() for word in line.split()]

    print(f"Сумма чисел в файле {path} : {sum(num_list)}")

except IOError:
    print("Произошла ошибка ввода-вывода!")
